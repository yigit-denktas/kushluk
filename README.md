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
- **Deterministic publication pipeline.** AI can research, rank, and write; rendering and print validation remain deterministic.
- **Graceful degradation.** Missing integrations remove/degrade blocks rather than silently corrupting the edition.
- **Source discovery.** Connected accounts can help Kuşluk discover sources the user already chose, such as newsletters, while keeping final source selection explicit.

## Current status

**Stage 1 is active and executable.**

The current walking skeleton is:

`weather + calendar + RSS -> candidates -> clustering/ranking -> publication -> HTML -> validated PDF -> print/email -> archive`

Implemented:
- Python package and CLI;
- environment-based configuration;
- Open-Meteo weather;
- configurable RSS/Atom ingestion;
- generic ICS calendar connector with fixture fallback;
- canonical candidate/story/publication models;
- deterministic clustering, ranking and deduplication;
- optional-lead layout support without forcing a lead;
- typed failure records and run summaries;
- Markdown-first canonical edition;
- deterministic A4 HTML renderer;
- optional WeasyPrint PDF output;
- one-page PDF validation with editorial cut/retry passes;
- CUPS printer capability detection and duplex-aware printing;
- optional SMTP delivery and email-on-print-failure;
- local edition archive and archive listing;
- runtime `doctor` command;
- tests and GitHub Actions CI;
- CI walking-skeleton smoke test;
- manually dispatchable sample-edition workflow.

Not complete yet:
- a real local printer trial;
- a real personal calendar/task connection beyond generic ICS;
- configured SMTP credentials if email delivery is wanted;
- multiple real morning editions and reading-feedback trials;
- newsletter discovery connector implementation;
- X/social inputs;
- final production visual system.

See [docs/STATUS.md](docs/STATUS.md) for the live implementation boundary and [docs/OPEN_DECISIONS.md](docs/OPEN_DECISIONS.md) for decisions that are intentionally not being made automatically.

## Quick start

Requires Python 3.11+.

```bash
git clone https://github.com/yigit-denktas/kushluk.git
cd kushluk

python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

kushluk doctor
kushluk generate --no-pdf
```

For validated PDF output:

```bash
pip install -e ".[pdf]"
kushluk generate
```

For local CUPS printing:

```bash
kushluk generate --print
```

For configured SMTP delivery:

```bash
kushluk generate --email
```

For print with email fallback:

```bash
kushluk generate --print --email-on-print-failure
```

To inspect recent local editions:

```bash
kushluk archive-list
```

Copy the relevant values from `.env.example` into the runtime environment to configure location, RSS sources, ICS calendar, printer, archive/output paths, or SMTP delivery.

## Project memory

Repository documentation is durable project memory for future maintainers and orchestrator agents.

Start with:

- [AGENTS.md](AGENTS.md)
- [docs/STATUS.md](docs/STATUS.md)
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
