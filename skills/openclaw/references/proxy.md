# Debug Proxy Reference

Target release: OpenClaw 2026.4.29.

`openclaw proxy` runs the OpenClaw debug proxy and inspects captured traffic. Use it for transport debugging, provider/channel capture analysis, and reproducing network behavior around a child command.

## Commands

```bash
openclaw proxy start
openclaw proxy run -- openclaw doctor
openclaw proxy coverage
openclaw proxy sessions
openclaw proxy query <preset>
openclaw proxy blob <id>
openclaw proxy purge
```

## Run Example

```bash
openclaw proxy run --host 127.0.0.1 --port 18080 -- openclaw channels status --probe
```

`proxy run` starts capture and runs the child command passed after `--`.

## Subcommands

| Command | Purpose |
|---|---|
| `start` | Start the local explicit debug proxy |
| `run` | Run a child command with capture enabled |
| `coverage` | Report transport coverage and gaps |
| `sessions` | List recent capture sessions |
| `query` | Run a built-in query preset |
| `blob` | Read a captured payload blob by ID |
| `purge` | Delete captured traffic metadata and blobs |

## Cautions

- Captures can contain tokens, message content, URLs, and provider payloads.
- Use `purge` after collecting the evidence you need.
- Do not paste raw captured blobs into public issues without redaction.
- Bind to loopback unless a trusted debugging setup requires otherwise.

## Related References

- [gateway_ops.md](gateway_ops.md) — gateway operation and logs
- [channel_troubleshooting.md](channel_troubleshooting.md) — channel failure signatures
- [security.md](security.md) — sensitive local logs and secrets
