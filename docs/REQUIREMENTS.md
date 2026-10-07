# Requirements

Normative terms **MUST**, **SHOULD**, and **MAY** are used intentionally.

## Product

- The system **MUST** generate a personalised daily briefing.
- The canonical edition geometry **MUST** be four logical DIN A4 pages.
- The editorial/layout model **MUST NOT** fork into separate A4 and A3 designs solely because of printer paper size.
- The system **MUST** support an A4 Home Printer profile using two A4 sheets, preferably duplex.
- The system **MUST** support an A3 Folded Newspaper profile using one duplex A3 landscape sheet imposed as outside `4 | 1` and inside `2 | 3`, then half-folded to A4.
- Single-sided A4 printing **MUST** be allowed when duplex is unavailable.
- The edition **MUST** target readiness by 08:00 local time by default.
- The target reading time **SHOULD** be 10–15 minutes; this is a soft target, not a hard truncation rule.
- The system **MUST NOT** force a lead story when no story deserves that treatment.

## Edition hierarchy

- Page 1 and the early reading flow **SHOULD** emphasise practical "Today" material and immediate orientation.
- Later page budget **SHOULD** allow more personal/editorial "For You" material.
- The exact four-page archetype **MAY** vary with the day's content; page geometry remains fixed.
- Calendar and task commitments **MUST** outrank detailed travel information on the printed page.
- Volatile travel details **SHOULD** be reduced to stable reminders, identifiers, or pointers to live apps.

## Core content capabilities

The system **MUST** be able to represent:
- weather;
- calendar;
- tasks;
- selected news/editorial stories;
- source links and QR destinations;
- explicit failure/unavailability states;
- media assets with provenance, attribution, dimensions, crop/focal-point metadata, and suitability state.

The architecture **SHOULD** support later:
- newsletters;
- X/social inputs;
- Reddit;
- Hacker News;
- email-derived signals;
- language-learning columns;
- idioms/proverbs;
- personal astrology calculated from an ephemeris;
- cartoons/illustration;
- travel-aware delivery;
- external AI briefing inputs as non-authoritative candidate generators.

## Source behaviour

- Sources **MUST** be implemented behind connectors/adapters.
- No single social or AI provider **MAY** become a hard dependency for the core publication loop.
- X content **SHOULD** be supported early because it is a desired input, but the integration **MUST** remain isolated from the canonical editorial model.
- External AI briefings **MAY** suggest candidates but **MUST NOT** be treated as authoritative sources without verification.

### Newsletter discovery and use

- Email/newsletter ingestion **MUST** require an explicitly connected email account.
- Newsletter discovery **SHOULD** inspect only a bounded recent mailbox window rather than indexing the entire mailbox.
- Discovery/classification **SHOULD** occur inside the user's personal data plane by default.
- Detected newsletters **MUST** be presented to the user before becoming persistent editorial sources.
- A user **MUST** be able to select a per-newsletter mode.
- Supported modes **SHOULD** include at least:
  - Ignore;
  - Reference only / use as a source signal;
  - Derivative / editorial synthesis;
  - Personal-copy / direct inclusion.
- Newly detected newsletters **MUST NOT** silently become trusted sources.
- Newsletter-derived items **MUST** retain attribution and an original source/message reference where technically possible.
- Direct inclusion **MUST NOT** be treated as permission to publicly redistribute a publisher's content.
- Shared/public/managed publication modes **MUST** apply stricter reuse rules than a user's private local edition.
- A newsletter subscription **MUST NOT** guarantee a print slot; the normal editorial cut/ranking system still applies.

## Personalisation

- A user **MUST** be able to declare initial interests/beats.
- The system **MAY** accept an optional spoken or typed edition-scoped morning intent.
- Morning intent **MUST NOT** silently become a durable preference.
- Morning intent **MUST NOT** bypass source verification, privacy boundaries, or required practical content.
- Beats **MUST** be omittable when nothing material happened.
- Personalisation **MUST NOT** require recurring manual exports, tagging, or preference maintenance.
- The user model **MUST** remain provider-independent and inspectable.
- The system **SHOULD** later learn from privacy-preserving passive signals.
- A protected serendipity mechanism **MUST** allow important or interesting material outside the established profile.

## Language

- Language preferences **MUST** be configurable in natural terms.
- The system **MUST** support a single-language edition mode.
- The system **MAY** intentionally mix languages within or across sections.
- Language mixing **MUST** be deliberate, not accidental model drift.

## Automation and orchestration

- The mature daily run **MUST** be executable without opening a visual editor or manually placing stories/images.
- The core application **MUST** expose a stable trigger boundary usable by CLI, OS schedulers, workflow engines such as n8n, and control surfaces such as Apple Shortcuts.
- External orchestrators **MUST NOT** become the canonical store for ranking rules, publication state, layout geometry, or edition history.
- Scheduled/retried runs **SHOULD** be idempotent for an edition and **MUST NOT** silently create duplicate print jobs.
- The system **SHOULD** expose machine-readable run states and material failures.

## Travel and delivery

- Travel detection **SHOULD** be derived from reliable user context such as calendar/travel documents when available.
- When the user is away from the configured print location, the system **SHOULD** avoid unnecessary home printing.
- Digital fallback by email **MUST** be supported before messaging-channel delivery becomes required.
- Messaging delivery **MAY** be added later.
- If location is unknown, weather **SHOULD** fall back to a configured default location rather than creating an empty block.

## Privacy and deployment

- Local/self-hosted operation **MUST** be the default.
- Personal data **MUST** remain within the user's personal data plane unless an explicitly configured connector requires a minimum subset.
- Telemetry **MUST** be off by default.
- The system **MUST NOT** require a central behavioural database.
- A future managed-cloud mode **MAY** exist but **MUST** be treated as a distinct operating mode with explicit privacy/compliance design.

## Rendering, assets, and print

- Rendering **MUST** be deterministic after the publication/layout manifest is finalised.
- The renderer **MUST** produce four logical A4 pages before print-profile imposition.
- Layout overflow **MUST** be detected per page before printing.
- Content cuts or archetype substitutions **MUST** occur before reducing typography below readability thresholds.
- Image assets **MUST** be validated for target-slot geometry and effective print resolution; unsuitable images **MUST** fall back safely rather than forcing a broken layout.
- The print subsystem **MUST** use an adapter boundary.
- Physical imposition **MUST** belong to the print layer rather than editorial reasoning.
- CUPS/`lp` is the preferred initial local print backend.
- The system **SHOULD** query printer capabilities where possible.
- The system **MUST NOT** assume the printer can identify paper colour, stock, or intent automatically.
- Paper characteristics **SHOULD** be represented as explicit user/configuration profiles.

## Failure behaviour

- Material failures **MUST** be explicitly surfaced to the user.
- Failures **MUST** be typed/categorised.
- Partial source failures **MUST NOT** leave blank layout blocks.
- Core-context failures such as calendar unavailability **SHOULD** trigger a user-visible notification.
- A failed print **MUST NOT** destroy the generated digital edition.
- Failure behaviour is further defined in `FAILURE_MATRIX.md`.

## Archive and identity

- Every edition **MUST** have a stable identifier.
- Edition identifiers **SHOULD** contain date plus a monotonically increasing or otherwise unique edition component.
- Stories **SHOULD** have stable IDs suitable for cross-edition references.
- Canonical archives **SHOULD** preserve Markdown plus structured metadata, with rendered HTML/PDF as derived artefacts.
- Later editions **SHOULD** be able to reference prior editions/stories.

## Stage 1 acceptance boundary

Stage 1 **MUST** produce, without hand-editing HTML:

`real input(s) -> canonical candidates -> ranked publication -> four logical A4 pages -> validated PDF -> selected print profile/digital result -> archive`
