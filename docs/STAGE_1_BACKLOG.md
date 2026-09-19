# Stage 1 Backlog — Walking Skeleton

## Stage outcome

Produce a real DIN A4 Kuşluk edition end to end with no hand-edited HTML.

## Epic 1 — Repository foundation

### Features
- Python project structure
- configuration model
- `.env.example`
- local data/output paths
- test harness
- formatter/linter
- CI basics later if useful

### Acceptance
- fresh clone can install and run locally from documented commands;
- no secrets committed;
- config errors are explicit.

## Epic 2 — Canonical models

### Features
Define schemas for:
- Source
- Candidate
- StoryCluster
- PracticalItem
- Publication
- EditionMetadata
- DeliveryResult
- Failure

### Acceptance
Provider-specific fields do not leak into core editorial schemas.

## Epic 3 — Initial connectors

### Weather
Use a reliable source for configured default location.

### Calendar
Start with fixture/ICS boundary; replace with a live connector once publication loop works.

### Public stories
Use one open RSS/feed path for at least three current stories.

### X experiment
Investigate the Grok/X route desired by the founding user, but keep it behind an optional connector. Stage 1 must still work without it.

### Acceptance
Each connector can fail independently without breaking unrelated connectors.

## Epic 4 — Normalisation and ranking

### Features
- canonical candidate conversion;
- deduplication;
- minimal story clustering;
- explainable ranking v0;
- optional lead;
- protected serendipity slot.

### Acceptance
For every selected story, debug output can explain why it was selected.

## Epic 5 — Publication model

### Features
- Markdown-first edition;
- metadata sidecar/model;
- Today / For You surfaces;
- source references;
- QR/link placeholders;
- edition ID.

### Acceptance
The canonical publication is useful without the HTML renderer.

## Epic 6 — Deterministic renderer

### Suggested stack
- Jinja2
- print CSS
- WeasyPrint

### Features
- DIN A4;
- front/back support;
- single-sided fallback;
- paper profile token;
- monochrome-safe style;
- design skeleton inspired by the design brief, not by generic UI cards.

### Acceptance
Same publication model + same template yields the same layout.

## Epic 7 — Validation and cut loop

### Validate
- expected page count;
- no overflow;
- readable minimum type sizes;
- required blocks;
- basic link integrity.

### Cut order
Use `EDITORIAL_SYSTEM.md`.

### Acceptance
Overflow triggers editorial cuts and rerendering rather than uncontrolled font shrinking.

## Epic 8 — Printing

### Initial backend
CUPS / `lp`.

### Features
- configured printer;
- capability detection where available;
- duplex when supported;
- single-sided fallback;
- explicit job result;
- preserve PDF if print fails.

### Acceptance
A local test edition reaches the configured printer or produces a typed delivery error.

## Epic 9 — Digital fallback

### V1
Email.

### Acceptance
When print delivery fails, the generated edition remains accessible and a configured email fallback can deliver it.

## Epic 10 — Archive

Store locally:
- publication Markdown;
- metadata;
- rendered HTML;
- PDF where configured;
- failure/delivery summary.

### Acceptance
An earlier edition can be located by edition ID and referenced from a later edition.

## First executable milestone

Use:
- real weather for Köln/default location;
- a calendar fixture;
- three current RSS stories.

Produce:
- canonical publication;
- A4 HTML;
- validated PDF;
- print attempt;
- local archive.

Then replace fixtures with real personal connectors.

## Reality trial

After the first print, run at least five real editions before expanding scope aggressively.

Record:
- what was actually read;
- what was consistently ignored;
- layout pain;
- missing practical context;
- source failures;
- generation time;
- printer reliability.

Use this evidence to reprioritise Stage 2.
