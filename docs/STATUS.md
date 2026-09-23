# Kuşluk Status

Last updated: 2026-09-23.

## Repository hygiene

- Default branch: `main`.
- Working branches: none.
- Open pull requests: none.
- Closed/merged pull requests: none found.
- Current work is committed directly to `main`; there is no dangling review branch or active PR.
- CI on the current Stage 1 implementation is expected to remain green before work is considered settled.

GitHub pull-request objects are historical records and are not normally "deleted" after merge; Kuşluk currently has no PR records to clean up anyway.

## Stage status

### Stage 0 — Product definition

Effectively complete for implementation purposes.

The product, requirements, architecture, editorial rules, design direction, privacy boundary, onboarding, failure policy, upstream policy, roadmap and ADRs are recorded.

Unresolved choices are isolated in `OPEN_DECISIONS.md` rather than blocking unrelated work.

### Stage 1 — Walking skeleton

**Active. Software path implemented; physical/local proof pending.**

Executable path:

`weather + calendar + RSS -> canonical candidates -> clustering/ranking -> publication -> A4 HTML -> validated PDF -> print/email -> archive`

Available commands:

- `kushluk doctor`
- `kushluk generate --no-pdf`
- `kushluk generate`
- `kushluk generate --print`
- `kushluk generate --email`
- `kushluk generate --print --email-on-print-failure`
- `kushluk archive-list`

## Implemented

### Inputs
- Open-Meteo weather;
- RSS/Atom;
- generic ICS calendar;
- calendar fixture fallback.

### Editorial core
- canonical candidates;
- transparent ranking;
- deterministic near-duplicate story clustering;
- source-cluster awareness;
- no forced lead story.

### Publication
- stable edition ID;
- Markdown canonical edition;
- deterministic A4 HTML;
- warm editorial v0 CSS;
- optional PDF rendering.

### Reliability
- typed failures;
- graceful source degradation;
- one-page PDF validation;
- editorial cut/retry rather than typography shrinking;
- overflow PDF kept as debug output rather than printed.

### Delivery
- CUPS printer discovery/capabilities;
- duplex-aware print submission;
- generic SMTP delivery;
- email fallback when printing is explicitly requested and fails.

### Archive / operations
- Markdown, JSON, HTML and validated PDF archive;
- run/failure/delivery summary;
- archive listing;
- runtime doctor;
- CI tests, linting and full walking-skeleton smoke test.

## Intentionally not completed automatically

### Needs a product/design decision
- whether the A3 105/210/105 gatefold supersedes A4 duplex or remains an extended format;
- final production typefaces / locked print design.

### Needs local/private setup
- the machine/server that runs Kuşluk at 08:00;
- access to the real printer;
- a real personal calendar/task source;
- SMTP credentials if email is enabled;
- any X/social credentials or provider setup.

### Needs evidence from real use
- real printer error mapping;
- final editorial density;
- reading-time calibration;
- paper-stock behaviour;
- serendipity tuning;
- five-edition reality trial.

## Next decision boundary

No further architecture decision is required to run the current A4 walking skeleton.

The next consequential product decision is the **canonical physical format**:
- A4 duplex remains default; A3 gatefold is an optional/extended edition, or
- A3 gatefold supersedes ADR 0002 and becomes the default physical object.

Until that is decided, implementation continues to respect the accepted A4 default.
