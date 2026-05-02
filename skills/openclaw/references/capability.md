# Capability / Infer Reference

Target release: OpenClaw 2026.4.29.

`openclaw infer` and its alias `openclaw capability` expose provider-backed inference through a stable CLI surface. Use this for direct text, image, audio, TTS, video, web, and embedding operations without running a full chat agent turn.

## Command Tree

```bash
openclaw infer list
openclaw infer inspect <capability-id>
openclaw infer model run --prompt "Summarize this"
openclaw infer image generate --prompt "diagram of a gateway" --output out.png
openclaw infer image describe --file ./image.png
openclaw infer audio transcribe --file ./voice.m4a
openclaw infer tts convert --text "hello" --output hello.mp3
openclaw infer video generate --prompt "short product shot"
openclaw infer web search --query "OpenClaw docs"
openclaw infer embedding create --text "memory text"
```

`openclaw capability ...` is equivalent to `openclaw infer ...`.

## Major Surfaces

| Surface | Purpose |
|---|---|
| `list` | List canonical capability IDs and supported transports |
| `inspect` | Inspect one canonical capability ID |
| `model` | Text inference and model catalog commands |
| `image` | Image generation, editing, description, and providers |
| `audio` | Audio transcription |
| `tts` | Text-to-speech conversion, voices, providers, personas |
| `video` | Video generation, description, and providers |
| `web` | Web search/fetch capabilities |
| `embedding` | Embedding creation and providers |

## Image Example

```bash
openclaw infer image generate \
  --prompt "clean operations dashboard screenshot" \
  --model openai/gpt-image-2 \
  --resolution 1K \
  --output dashboard.png
```

Common image flags in 2026.4.29:

| Flag | Meaning |
|---|---|
| `--prompt <text>` | Prompt text |
| `--file <path>` | Input file for model/image/audio commands that accept files |
| `--model <provider/model>` | Model override |
| `--count <n>` | Number of images |
| `--output <path>` | Output path |
| `--resolution <value>` | `1K`, `2K`, or `4K` hint |
| `--size <size>` | Size hint such as `1024x1024` |
| `--aspect-ratio <ratio>` | Ratio hint such as `16:9` |
| `--output-format <format>` | `png`, `jpeg`, or `webp` |
| `--timeout-ms <ms>` | Provider request timeout |

## When To Use

- Test model/provider auth without invoking the agent loop.
- Generate or inspect media for an operations workflow.
- Probe provider capability availability after changing auth profiles.
- Build automation that needs a narrow provider operation.

## Related References

- [providers.md](providers.md) — model providers and auth profiles
- [model_failover.md](model_failover.md) — failover behavior
- [media.md](media.md) — media handling in agent/channel workflows
- [web_tools.md](web_tools.md) — web search/fetch tools
