# Data Map

## Principle

Store the minimum durable personal state needed to make Kuşluk useful.

Raw personal data stays inside the user's personal data plane by default.

## Data classes

### 1. Configuration
Examples:
- home/default location;
- edition time;
- languages;
- selected beats;
- printer;
- paper profile;
- delivery channels;
- pause/travel behaviour;
- per-newsletter source modes and priorities.

Retention: until user changes/deletes it.

### 2. Secrets and tokens
Examples:
- calendar OAuth;
- email OAuth;
- social connector credentials;
- API keys.

Storage: dedicated local secret mechanism; never Git.

Retention: until revoked/deleted.

### 3. Calendar/tasks
Prefer event/task metadata and bounded retrieval windows.

Do not build a permanent calendar corpus unless a feature explicitly requires it.

### 4. Email/newsletters

Separate:
- operational email metadata/signals;
- discovered newsletter/source inventory;
- newsletter content intentionally used as editorial source.

Newsletter discovery should be incremental and bounded.

A discovered newsletter source record may contain:
- sender/publication identity;
- sender address/domain;
- mailing-list identifiers where available;
- recent delivery/frequency metadata;
- classification confidence;
- user-selected source mode;
- user-selected priority;
- original message/source references.

Raw newsletter bodies should not be retained indefinitely by default.

For derivative mode, retain only what is needed for provenance, deduplication, archive references, and reproducibility.

For personal-copy/direct-inclusion mode, raw content may be processed locally for the user's private edition, but this must not be treated as public redistribution permission.

Do not mirror the user's entire mailbox into Kuşluk by default.

### 5. Social signals
Possible future inputs:
- explicit saves/bookmarks;
- selected followed sources;
- recent relevant activity exposed by a connector;
- user-authorised preference signals.

Do not require recurring manual exports.

### 6. User model
Derived local state, for example:
- topic affinities;
- source affinities;
- language preferences;
- reading density;
- negative preferences;
- recent-topic saturation.

Must be inspectable, exportable, and deletable.

### 7. Public candidates
News/RSS/web items may be cached locally for editorial processing.

Cache should record source URL, retrieval time, and source identity.

### 8. Editions
Each edition should preserve:
- edition ID;
- generation timestamp;
- target date/timezone;
- publication Markdown;
- structured metadata;
- story IDs;
- source references;
- delivery outcome;
- validation result.

HTML/PDF are derived artefacts and may be regenerated where deterministic inputs are preserved.

## Edition identity

Recommended shape:

`YYYY-MM-DD · Edition NNN`

Machine ID may use:

`YYYYMMDD-NNN`

If multiple editions are generated in one day, the serial disambiguates them.

## Story identity

A story needs a stable identifier that can survive wording changes.

Prefer a generated stable ID tied to the canonical story cluster rather than headline text.

## Cross-edition references

Markdown should support explicit references, for example:

`[[edition:20260711-042]]`

`[[story:stargate-2026-01]]`

A renderer can convert these into hyperlinks, compact print references, or QR targets.

## External processing boundary

Public information may be sent to external research/LLM services.

Personal information may leave the device only when:
1. the user configured the connector/service;
2. the data is necessary for that action;
3. the minimum useful subset is sent.

Derived personal state remains sensitive even when it is not raw source data.

Newsletter contents are personal mailbox data even when the underlying newsletter is publicly available elsewhere. Prefer local parsing/classification and minimum necessary external disclosure.

## Deletion

Users must be able to remove:
- credentials;
- discovered newsletter/source inventory;
- retained newsletter content;
- source caches;
- user model;
- edition archive;
- feedback history.

Deletion should not depend on contacting a central Kuşluk service in local/self-hosted mode.
