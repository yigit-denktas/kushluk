# AGENTS.md

This file is durable project memory for human maintainers and orchestrator agents.

## Mission

Build **Kuşluk**, a local-first, print-first personal daily newspaper that turns a user's day, interests, and trusted information sources into a concise morning edition.

The project must remain useful when the original user, original conversation, original LLM provider, or original integration disappears.

## Non-negotiable product principles

1. **Local-first personal data plane.** Personal data remains on infrastructure controlled by the user by default.
2. **Print-first.** The physical morning edition is the primary product surface.
3. **One DIN A4 sheet by default.** Prefer duplex; allow single-sided fallback when hardware cannot duplex.
4. **08:00 local target.** The edition should be ready by 08:00 local time unless the user configures another time.
5. **Selection over collection.** The product is an editor, not a feed reader.
6. **Reliability before cleverness.** A modest edition that arrives is better than a brilliant edition that fails.
7. **Provider independence.** LLM, search, social, mail, calendar, weather, printer, and delivery systems are adapters.
8. **Deterministic rendering.** Generative systems may prepare content, but layout validation and printing must be deterministic.
9. **Graceful degradation.** Missing data removes or replaces a block; it must never create silent holes or corrupt layout.
10. **No recurring manual data labour.** Personalisation may ask for initial preferences, but must not depend on routine manual exports, tagging, or curation.
11. **Serendipity is intentional.** Protect space for material outside the user's existing interest bubble.
12. **Archive is first-class.** Editions and stories need stable identifiers and durable references.

## Documentation precedence

When documents conflict, resolve in this order:

1. Accepted ADRs under `docs/adr/`
2. `docs/REQUIREMENTS.md`
3. `docs/PRODUCT.md`
4. `docs/ARCHITECTURE.md`
5. `docs/EDITORIAL_SYSTEM.md`
6. `docs/DESIGN_BRIEF.md`
7. `docs/ROADMAP.md` and implementation backlog

`docs/OPEN_DECISIONS.md` records unresolved choices and never overrides accepted ADRs.

Do not silently reinterpret a recorded decision. Propose a new ADR when changing architecture or a non-trivial product invariant.

## Working method

Use vertical slices. Prefer a working bicycle over disconnected car parts.

For each stage:
- state the user-visible outcome;
- define acceptance criteria;
- implement the smallest end-to-end path;
- test with real editions;
- record what changed and why;
- only then deepen integrations.

## Current implementation

Stage 1 is active and the software walking skeleton is executable.

Current path:

`Open-Meteo + ICS/fixture calendar + RSS -> canonical candidates -> clustering/ranking -> publication -> A4 HTML -> optional validated PDF -> CUPS/SMTP -> archive`

Implemented infrastructure includes:
- typed failures and run summaries;
- deterministic story clustering and ranking;
- optional lead support with no forced lead;
- one-page PDF validation and editorial cut/retry;
- printer capability/duplex detection;
- SMTP delivery and print-failure fallback;
- archive listing;
- runtime doctor;
- CI lint/tests plus an end-to-end smoke test.

Do not claim Stage 1 is finished until a real local print path and repeated real-edition trial have been completed.

## Stage 1 boundary

The implementation must prove:

`real inputs -> normalized candidates -> publication model -> deterministic A4 HTML -> PDF -> printer/digital fallback -> archive`

The code path now exists. Remaining proof depends mainly on real local connectors, printer access, and repeated usage.

Do not build a broad agent platform before this loop is proven in reality.

## Privacy boundary

Public information may be researched externally. Personal context must not be sent to third-party services unless a connector explicitly needs the minimum required subset and the user has configured it.

A future managed-cloud product is allowed, but it is a separate operating mode with its own privacy/compliance obligations. Do not weaken local-first defaults to make managed hosting easier.

Calendar URLs may contain private tokens; do not persist full private ICS URLs into edition/source metadata.

SMTP credentials belong in environment/runtime secret storage, never Git.

## Upstream reuse

Reuse permissively licensed upstream components when they save time, but:
- preserve Kuşluk's product and editorial layer;
- record reused code or substantial adapted material in `THIRD_PARTY_NOTICES.md`;
- preserve required copyright/license notices;
- do not make an upstream project a hard product dependency without an ADR.

See `docs/UPSTREAM_REVIEW.md` before introducing a new upstream dependency.

## Stop conditions / decisions

Do not make choices recorded in `docs/OPEN_DECISIONS.md` on the user's behalf.

External credentials, a local deployment host, and physical printer access are setup prerequisites rather than reasons to redesign the architecture.

## Naming

Repository: `kushluk`

Product working name: **Kuşluk**

The name may change later. Do not block implementation on branding.
