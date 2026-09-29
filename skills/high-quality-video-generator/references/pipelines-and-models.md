# Video pipelines and model catalog

## Agent skill repos distilled

### OpenMontage — `calesthio/OpenMontage` (~60k stars, AGPLv3)

Agentic production system. 12 pipelines, 100+ tools, 700+ skill files.

Pipelines worth mirroring here:

- Animated explainer
- Documentary montage (real stock + VO)
- Cinematic trailer
- Talking head
- Motion graphics
- Clip factory / shorts
- Podcast repurpose
- Localization and dub

Canonical stage order: research → proposal → script → scene plan → assets → edit → compose.

Free path they document: Piper TTS, FFmpeg, Remotion / HyperFrames, Pexels, Archive.org.
GPU optional: Wan 2.2, Hunyuan.

### Hypit — `hypit-ai/hypit` (~11.6k stars)

Install in other agents: `npx skills add hypit-ai/hypit -g`

SVML = composition anchored to words. Clone a video's workflow (footage slots, captions, B-roll, effects), then swap the payload and ship variants.

### Other agent skills

- `GoldLegendW80/llm-video-maker` — prompt to MP4, captions, VO, HyperFrames-style HTML render
- `realaman90/ai-film-skills` — short-film stack (image models + Veo/Seedance/LTX + ElevenLabs + assembly)
- `genra-ai/video-creator` — script-to-video skill pack
- `nexu-io` html-video — HTML/CSS/GSAP → MP4
- `Anil-matcha/vox-ai-motion-graphics-generator` — Vox-style collage explainers

## Open video models

| Model | Repo / org | Notes |
| Open-Sora 2.0 | hpcaitech | highest-star open T2V lineage |
| CogVideoX | zai-org/CogVideo | Diffusers, ~16 GB |
| LTX-Video | Lightricks/LTX-Video | speed |
| Wan 2.2 | Alibaba Tongyi | 1.3B ~8 GB, 14B ~24 GB |
| HunyuanVideo | Tencent | 720/1080, 60–80 GB class |

## In-session tool map

| Need | Tool |
| designed motion + captions | HyperFrames compose |
| stills / character sheets | generate_image, edit_image |
| reference frames | search_images |
| VO / lyric scratch | voice_list_voices, voice_generate_speech |
| cut, mix, caption burn, conform | ffmpeg skill |
| music bed | full-song-generator skill + user renderer |

## Aspect and length defaults

- TikTok / Reels / Shorts — 9:16, 15–45 s
- YouTube explainer — 16:9, 60–180 s
- Trailer — 16:9, 15–30 s
- Music visualizer — match song duration, cut on beats from `[Tempo]`

## Scored-job config keys

Mirror the song skill genre dict when boarding a music video:

```
style, tempo, key, atmosphere
```

Persist those four fields plus the section list (`Intro`, `Verse 1`, `Chorus`, ...) at the top of `SHOTS.md`. Cut duration for a section ≈ bars in that section × 4 × (60 / BPM) for 4/4. Waltz uses 3 beats per bar.
---
