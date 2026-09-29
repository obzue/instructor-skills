# Full-song model catalog (GitHub, 2026)

Pick one renderer. Do not list this whole file to the user unless they ask.

## YuE / YuE2 — lyrics2song foundation

- Repo: https://github.com/multimodal-art-projection/YuE (~9.8k stars)
- Weights: Hugging Face `m-a-p/YuE2-3B`, VAE `m-a-p/YuE2-Vae`
- What it does: style sentence + lyrics → symbolic ABC plan → 48 kHz stereo song with vocal and accompaniment
- Modes: `cot=full` new song, `cot=melody` cover from ABC, `cot=off` no plan
- Hardware: Linux, Python 3.12, NVIDIA BF16, 24 GB VRAM minimum
- License: code Apache 2.0, weights CC BY-NC 4.0 (check before commercial use)
- ComfyUI: `smthemex/ComfyUI_YuE`, YuE2 nodes `o-l-l-i/ComfyUI-Olm-YuE2`

Python sketch:

```python
from yue2 import YuE2Pipeline
with YuE2Pipeline.from_pretrained("m-a-p/YuE2-3B", device="cuda") as pipe:
    song = pipe(lyrics=open("LYRICS.txt").read(), style=open("YUE_STYLE.txt").read(), cot="full")
    song.save_artifacts("outputs/my-song")
```

## ACE-Step 1.5 — strongest local Suno-class model

- Repo: https://github.com/ace-step/ACE-Step-1.5 (~12.8k stars, MIT)
- UI: https://github.com/fspecii/ace-step-ui
- Input: tags + lyrics; optional reference audio; 10 s–600 s
- Hardware: Mac MLX, CUDA, ROCm, Intel XPU; usable under 4 GB VRAM with offload/INT8; XL happier at 12–20 GB
- Features: covers, vocal-to-BGM, stem split, LoRA, LRC

## Tencent SongGeneration (LeVo)

- Repo: https://github.com/tencent-ailab/songgeneration
- Paper: LeVo — High-Quality Song Generation with Multi-Preference Alignment
- Full-length songs up to about 4m30s, vocals + accompaniment
- Studio UI: https://github.com/BazedFrog/SongGeneration-Studio (10 GB VRAM class)

## DiffRhythm

- Fast latent-diffusion lyrics-to-full-song (vocals + accompaniment together)
- Strong when latency matters more than editable score

## HeartMuLa / HeartMuse

- Repo: https://github.com/strnad/HeartMuse
- Local Gradio; LLM writes lyrics/tags; HeartMuLa renders up to ~240 s

## SongComposer

- Repo: https://github.com/pjlab-songcomposer/songcomposer
- Symbolic lyric + melody LLM (ACL 2025). Good when the user wants readable notes, not a mix.

## Routing cheat sheet

| Goal | Pick |
| new full mix, editable score | YuE2 cot=full |
| consumer GPU / Mac | ACE-Step 1.5 |
| Tencent research quality | LeVo / SongGeneration |
| fastest diffusion song | DiffRhythm |
| lyrics+tags UI locally | HeartMuse |
| lead sheet only | SongComposer |
---
