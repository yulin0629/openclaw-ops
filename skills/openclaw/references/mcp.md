# MCP Reference

Target release: OpenClaw 2026.4.29.

`openclaw mcp` manages OpenClaw MCP config and exposes OpenClaw channels over MCP stdio. Use it when another assistant or MCP client needs to inspect or interact with OpenClaw channel context through a local MCP bridge.

## Commands

```bash
openclaw mcp list
openclaw mcp show
openclaw mcp show <name>
openclaw mcp set <name> '{"command":"node","args":["server.js"]}'
openclaw mcp unset <name>
openclaw mcp serve
```

## Serve Options

| Option | Use |
|---|---|
| `--url <url>` | Gateway WebSocket URL |
| `--token <token>` | Gateway token |
| `--token-file <path>` | Read gateway token from file |
| `--password <password>` | Gateway password |
| `--password-file <path>` | Read gateway password from file |
| `--claude-channel-mode <mode>` | Claude channel notification mode: `auto`, `on`, or `off` |
| `--verbose` | Verbose logging to stderr |

## Config Operations

- `list` shows configured MCP servers.
- `show` prints one configured server or the full MCP config.
- `set` writes one server from a JSON object.
- `unset` removes one configured server.
- `serve` exposes OpenClaw channels over stdio for an MCP client.

## Operations

- Prefer token/password files over shell history when credentials are needed.
- Use `--verbose` only while debugging; MCP stdio clients can be sensitive to unexpected stdout.
- Keep channel bridge access scoped to trusted local clients because it can expose channel context.

## Related References

- [channels.md](channels.md) — channel setup and account IDs
- [security.md](security.md) — gateway auth and local trust boundaries
- [slash_commands.md](slash_commands.md) — in-channel `/mcp` commands are separate from CLI `openclaw mcp`
