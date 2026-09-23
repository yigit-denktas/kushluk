# Stage 1 Backlog — Walking Skeleton

## Stage outcome

Produce a real DIN A4 Kuşluk edition end to end with no hand-edited HTML.

Status: **ACTIVE**

## Epic 1 — Repository foundation — IN PROGRESS

Implemented:
- Python project structure;
- configuration model;
- `.env.example`;
- local output/archive paths;
- test harness;
- Ruff/pytest CI;
- manually dispatchable sample-edition workflow.

Remaining:
- verify CI green on GitHub after each dependency/workflow change;
- improve install/runtime error messages as real environments expose them.

## Epic 2 — Canonical models — IN PROGRESS

Implemented:
- SourceRef;
- Candidate;
- PracticalItem;
- Story;
- Publication;
- stable edition identity.

Remaining:
- explicit StoryCluster model;
- typed Failure model;
- richer DeliveryResult;
- schema/versioning once real connectors begin producing durable archives.

## Epic 3 — Initial connectors — IN PROGRESS

Implemented:
- Open-Meteo weather;
- calendar fixture;
- configurable RSS/Atom connector.

Remaining:
- live calendar connector;
- task connector;
- source-specific error typing;
- optional X/Grok experiment behind a connector seam.

Acceptance remains: each connector must fail independently without breaking unrelated connectors.

## Epic 4 — Normalisation and ranking — IN PROGRESS

Implemented:
- canonical candidate conversion;
- title-level deduplication;
- explainable deterministic ranking v0.

Remaining:
- story clustering beyond title normalization;
- stronger source-quality inputs;
- optional lead decision;
- protected serendipity slot.

## Epic 5 — Publication model — IN PROGRESS

Implemented:
- Markdown-first edition;
- Today / For You surfaces;
- source references;
- edition ID;
- JSON archive metadata.

Remaining:
- explicit metadata schema version;
- QR/link representation in the canonical model;
- prior-edition/story references.

## Epic 6 — Deterministic renderer — IN PROGRESS

Implemented:
- Jinja2 A4 HTML template;
- print CSS;
- monochrome-safe warm editorial v0;
- optional WeasyPrint PDF rendering.

Remaining:
- front/back duplex templates;
- paper profile tokens;
- stronger production design implementation;
- print-geometry regression fixtures.

## Epic 7 — Validation and cut loop — NOT STARTED

Validate:
- expected page count;
- overflow;
- minimum readable type sizes;
- required blocks;
- basic link integrity.

Overflow must trigger editorial cuts/rerendering rather than uncontrolled font shrinking.

## Epic 8 — Printing — IN PROGRESS

Implemented:
- CUPS/`lp` adapter boundary;
- configured printer name;
- explicit print result;
- PDF preservation when printing is not attempted.

Remaining:
- printer capability detection;
- duplex selection;
- paper/offline error mapping;
- real printer trial.

## Epic 9 — Digital fallback — NOT STARTED

V1: email.

Acceptance:
When print delivery fails, the generated edition remains accessible and a configured email fallback can deliver it.

## Epic 10 — Archive — IN PROGRESS

Implemented:
- publication Markdown;
- structured JSON metadata;
- rendered HTML copy;
- PDF copy when available;
- stable edition directory.

Remaining:
- delivery/failure summary;
- lookup API;
- cross-edition references.

## First executable milestone

Current pipeline:

`Open-Meteo + calendar fixture + configurable RSS -> candidates -> ranking -> Markdown -> A4 HTML -> optional PDF -> optional CUPS -> archive`

Next engineering work that does not require a product decision:
1. add layout validation and cut/retry loop;
2. add typed failure model;
3. add printer capability detection;
4. replace calendar fixture with a live adapter;
5. add email digital fallback;
6. run multiple real editions and record failures.

## Reality trial

After the first successful local print, run at least five real editions before expanding scope aggressively.

Record:
- what was actually read;
- what was consistently ignored;
- layout pain;
- missing practical context;
- source failures;
- generation time;
- printer reliability.

Use this evidence to reprioritise Stage 2.
