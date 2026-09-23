# Kuşluk

**Kuşluk** is a local-first, print-first personal daily newspaper.

The project turns a user's day, interests, selected information sources, and public signals into a concise morning edition designed to be read away from a screen. The current canonical physical artifact is one DIN A4 sheet, ideally duplex, ready by 08:00 local time.

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
- **Source discovery.** Connected accounts can help Kuşluk discover information sources the user already chose, such as newsletters, while keeping final source selection explicit.

## Current status

**Stage 1 is active.**

The first executable walking skeleton is now in the repository:

`weather + calendar fixture + RSS -> canonical candidates -> ranking -> publication -> HTML -> optional PDF -> CUPS adapter -> archive`

Implemented:
- Python package and CLI;
- environment-based configuration;
- Open-Meteo weather connector;
- calendar fixture connector;
- RSS/Atom ingestion;
- canonical source/candidate/publication models;
- deterministic v0 ranking and deduplication;
- Markdown-first canonical edition;
- deterministic A4 HTML renderer;
- optional WeasyPrint PDF output;
- CUPS/`lp` print adapter;
- edition archive;
- tests;
- GitHub Actions CI;
- manually dispatchable sample-edition workflow.

Still deliberately incomplete:
- live personal calendar/task connector;
- layout overflow validation + editorial cut loop;
- email fallback;
- newsletter connector/onboarding implementation;
- X/social connectors;
- final production design system.

See [docs/OPEN_DECISIONS.md](docs/OPEN_DECISIONS.md) for the small number of product decisions that remain intentionally unresolved.

## Quick start

Requires Python 3.11+.

```bash
git clone https://github.com/yigit-denktas/kushluk.git
cd kushluk

python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

kushluk generate --no-pdf
```

For PDF output:

```bash
pip install -e ".[pdf]"
kushluk generate
```

To submit the generated PDF through local CUPS:

```bash
kushluk generate --print
```

Copy `.env.example` values into your runtime environment to change the configured location, RSS sources, archive/output paths, fixture path, or printer.

## Project memory

Repository documentation is treated as durable project memory so future maintainers and orchestrator agents can continue without relying on the founding conversation.

Start with:

- [AGENTS.md](AGENTS.md)
- [docs/PRODUCT.md](docs/PRODUCT.md)
- [docs/REQUIREMENTS.md](docs/REQUIREMENTS.md)
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/EDITORIAL_SYSTEM.md](docs/EDITORIAL_SYSTEM.md)
- [docs/DESIGN_BRIEF.md](docs/DESIGN_BRIEF.md)
- [docs/DATA_MAP.md](docs/DATA_MAP.md)
- [docs/ONBOARDING.md](docs/ONBOARDING.md)
- [docs/OPEN_DECISIONS.md](docs/OPEN_DECISIONS.md)
- [docs/UPSTREAM_REVIEW.md](docs/UPSTREAM_REVIEW.md)
- [docs/ROADMAP.md](docs/ROADMAP.md)
- [docs/STAGE_1_BACKLOG.md](docs/STAGE_1_BACKLOG.md)
- [docs/adr/](docs/adr/)

## License

MIT. See [LICENSE](LICENSE).

Third-party code, layouts, or ideas reused during implementation must be recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
