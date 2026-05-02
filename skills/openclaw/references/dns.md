# DNS Reference

Target release: OpenClaw 2026.4.29.

`openclaw dns` provides helpers for wide-area discovery, especially Tailscale plus CoreDNS setups that expose Bonjour/DNS-SD-style discovery beyond the local mDNS domain.

## Commands

```bash
openclaw dns setup
openclaw dns setup --help
```

The 2026.4.29 command surface focuses on setting up CoreDNS to serve a discovery domain for unicast DNS-SD (Wide-Area Bonjour).

## When To Use

- Gateway or node discovery must work across a tailnet instead of only local mDNS.
- Local Bonjour works on LAN but not across routed networks.
- You need a repeatable CoreDNS-backed discovery domain for remote nodes or clients.

## Operational Notes

- Confirm normal local discovery first with `openclaw gateway discover` and `openclaw system presence`.
- Keep Tailscale DNS/MagicDNS assumptions explicit; do not assume every device sees the same DNS view.
- Treat DNS setup as infrastructure state. Review generated CoreDNS config before deploying to a shared environment.

## Troubleshooting

```bash
openclaw gateway discover
openclaw system presence
dns-sd -B _openclaw-gw._tcp local.
```

If discovery fails only outside the LAN, inspect Tailscale DNS settings and CoreDNS forwarding before changing OpenClaw gateway auth or pairing state.

## Related References

- [bonjour.md](bonjour.md) — mDNS and DNS-SD details
- [presence_discovery.md](presence_discovery.md) — presence system and transports
- [remote_access.md](remote_access.md) — Tailscale and remote gateway access
