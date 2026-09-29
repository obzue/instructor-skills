#!/usr/bin/env bash
# Create an empty idea artifact folder.
set -euo pipefail
SLUG="${1:-}"
[[ -z "$SLUG" ]] && { echo "Usage: new_idea.sh <slug>"; exit 1; }
DIR="/home/workdir/artifacts/ideas/${SLUG}"
mkdir -p "$DIR"
cat > "$DIR/SPEC.md" << EOF
# ${SLUG}

## Problem

## Vision

## Out of scope

## Need

## Goal

## Claims

## Surface / Architecture

## Build order

## Risks

## Fog
EOF
echo "$DIR/SPEC.md"
