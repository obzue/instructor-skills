#!/usr/bin/env python3
"""Validate a lesson concept DAG and emit csv / mermaid / json."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,31}$")


def parse_md_table(text: str) -> list[dict]:
    rows = []
    lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return rows
    headers = [h.strip().lower() for h in lines[0].strip("|").split("|")]
    for line in lines[2:]:
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 2:
            continue
        rec = {headers[i]: cols[i] if i < len(cols) else "" for i in range(len(headers))}
        rows.append(rec)
    return rows


def split_ids(raw: str) -> list[str]:
    if not raw:
        return []
    return [p.strip() for p in re.split(r"[|,;\s]+", raw) if p.strip() and p.strip() != "-"]


def load_nodes(lesson: Path) -> list[dict]:
    js = lesson / "concepts.json"
    md = lesson / "CONCEPTS.md"
    nodes: list[dict] = []
    if js.exists():
        data = json.loads(js.read_text(encoding="utf-8"))
        nodes = data.get("nodes", data if isinstance(data, list) else [])
    elif md.exists():
        for rec in parse_md_table(md.read_text(encoding="utf-8")):
            nid = rec.get("id") or rec.get("conceptid") or ""
            if not nid:
                continue
            nodes.append(
                {
                    "id": nid,
                    "label": rec.get("name") or rec.get("label") or nid,
                    "prereq": split_ids(rec.get("prereq_ids") or rec.get("requires") or rec.get("prereq") or ""),
                    "helps": split_ids(rec.get("helps") or ""),
                    "bloom": rec.get("bloom") or "",
                    "evidence": rec.get("evidence") or "",
                    "status": rec.get("status") or "unknown",
                    "kind": rec.get("kind") or "",
                    "modality": rec.get("modality") or "text",
                }
            )
    else:
        raise SystemExit(f"no CONCEPTS.md or concepts.json in {lesson}")
    return nodes


def validate(nodes: list[dict]) -> list[str]:
    errors = []
    ids = [n["id"] for n in nodes]
    seen = set()
    for n in nodes:
        i = n["id"]
        if not ID_RE.match(i):
            errors.append(f"bad id {i!r}")
        if i in seen:
            errors.append(f"duplicate id {i}")
        seen.add(i)
        for field in ("prereq", "helps"):
            for p in n.get(field) or []:
                if p == i:
                    errors.append(f"{i} {field} self-edge")
                elif p not in seen and p not in ids:
                    errors.append(f"{i} {field} unknown {p}")
    # requires edge: B is prereq of A means teach B before A
    children = defaultdict(list)
    indeg = {i: 0 for i in ids}
    for n in nodes:
        for p in n.get("prereq") or []:
            if p in indeg:
                children[p].append(n["id"])
                indeg[n["id"]] += 1
    q = deque([i for i, d in indeg.items() if d == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in children[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != len(ids):
        stuck = [i for i, d in indeg.items() if d > 0]
        errors.append("cycle among: " + ", ".join(stuck))
    return errors


def topo(nodes: list[dict]) -> list[str]:
    ids = [n["id"] for n in nodes]
    children = defaultdict(list)
    indeg = {i: 0 for i in ids}
    for n in nodes:
        for p in n.get("prereq") or []:
            if p in indeg:
                children[p].append(n["id"])
                indeg[n["id"]] += 1
    q = deque(sorted(i for i, d in indeg.items() if d == 0))
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in sorted(children[u]):
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order


def longest_path(nodes: list[dict]) -> list[str]:
    order = topo(nodes)
    by = {n["id"]: n for n in nodes}
    dist = {i: 0 for i in by}
    pred = {i: None for i in by}
    children = defaultdict(list)
    for n in nodes:
        for p in n.get("prereq") or []:
            if p in by:
                children[p].append(n["id"])
    for u in order:
        for v in children[u]:
            if dist[u] + 1 > dist[v]:
                dist[v] = dist[u] + 1
                pred[v] = u
    if not dist:
        return []
    end = max(dist, key=dist.get)
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = pred[cur]
    path.reverse()
    return path


def emit(lesson: Path, nodes: list[dict]) -> None:
    order = topo(nodes)
    by = {n["id"]: n for n in nodes}
    roots = [n["id"] for n in nodes if not n.get("prereq")]
    children = defaultdict(list)
    for n in nodes:
        for p in n.get("prereq") or []:
            children[p].append(n["id"])
    sinks = [i for i in order if not children[i]]
    path = longest_path(nodes)

    csv_path = lesson / "learning-graph.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "label", "requires", "helps", "bloom", "evidence", "status", "modality"])
        for i in order:
            n = by[i]
            w.writerow(
                [
                    n["id"],
                    n.get("label", ""),
                    "|".join(n.get("prereq") or []),
                    "|".join(n.get("helps") or []),
                    n.get("bloom", ""),
                    n.get("evidence", ""),
                    n.get("status", "unknown"),
                    n.get("modality", "text"),
                ]
            )

    payload = {
        "title": lesson.name,
        "nodes": nodes,
        "order": order,
        "roots": roots,
        "sinks": sinks,
        "critical_path": path,
    }
    (lesson / "concepts.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def esc(s: str) -> str:
        return s.replace('"', "#quot;")

    lines = ["# Graph", "", f"- roots: {', '.join(roots) or '—'}", f"- sinks: {', '.join(sinks) or '—'}", f"- critical path: {' → '.join(path) or '—'}", "", "```mermaid", "flowchart TD"]
    for n in nodes:
        lines.append(f'  {n["id"]}["{esc(n.get("label") or n["id"])}"]')
    for n in nodes:
        for p in n.get("prereq") or []:
            lines.append(f"  {p} --> {n['id']}")
        for p in n.get("helps") or []:
            lines.append(f"  {p} -.-> {n['id']}")
    lines += ["```", "", "## Teach order", ""]
    for i, cid in enumerate(order, 1):
        n = by[cid]
        lines.append(f"{i}. `{cid}` {n.get('label','')} ({n.get('bloom') or 'bloom?'})")
    (lesson / "GRAPH.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("lesson")
    args = p.parse_args()
    lesson = Path(args.lesson)
    nodes = load_nodes(lesson)
    if not nodes:
        raise SystemExit("no concepts found")
    errors = validate(nodes)
    if errors:
        print("INVALID", file=sys.stderr)
        for e in errors:
            print("-", e, file=sys.stderr)
        sys.exit(1)
    emit(lesson, nodes)
    print(f"ok {len(nodes)} nodes -> {lesson / 'GRAPH.md'}")


if __name__ == "__main__":
    main()
