# Kuşluk

**Kuşluk** is a local-first, print-first personal daily newspaper.

The project turns a user's day, interests, selected information sources, and public signals into a concise morning edition designed to be read away from a screen. The default physical artifact is one DIN A4 sheet, ideally duplex, ready by 08:00 local time.

> Working principle: **selection over collection; reliability before cleverness.**

## Product direction

Kuşluk is being developed as an open, provider-independent system rather than a single AI-agent demo.

- **Local-first personal data plane.** Personal context stays on the user's device or infrastructure by default.
- **Print-first.** The primary surface is a compact physical edition; HTML, email, e-readers, and richer digital surfaces are secondary.
- **One sheet by default.** Front: practical “Today”. Back: personal “For You”. Single-sided fallback is allowed where duplex printing is unavailable.
- **Adaptive editorial system.** A lead story is optional. Calendar and tasks outrank volatile travel details. Space is protected for serendipity.
- **Multilingual by design.** Editions may use English, German, Turkish, other user-selected languages, or intentional language mixing.
- **Provider-independent user model.** The project must survive changes in LLM, search, social, mail, calendar, or printing providers.
- **Deterministic publication pipeline.** AI can research, rank, and write; rendering and print validation must remain deterministic.
- **Graceful degradation.** Missing integrations must not produce empty layout holes or silently broken editions.

## Current status

Stage 0 — product definition and architecture.

The repository documentation is intentionally treated as durable project memory so that future maintainers and orchestrator agents can continue the project without relying on the original conversation.

Start with:

- [AGENTS.md](AGENTS.md)
- [docs/PRODUCT.md](docs/PRODUCT.md)
- [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md)
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/EDITORIAL_SYSTEM.md](docs/EDITORIAL_SYSTEM.md)
- [docs/DESIGN_BRIEF.md](docs/DESIGN_BRIEF.md)
- [docs/DATA_MAP.md](docs/DATA_MAP.md)
- [docs/ROADMAP.md](docs/ROADMAP.md)
- [docs/STAGE_1_BACKLOG.md](docs/STAGE_1_BACKLOG.md)
- [docs/adr/](docs/adr/)

## License

MIT. See [LICENSE](LICENSE).

Third-party code, layouts, or ideas reused during implementation must be recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
