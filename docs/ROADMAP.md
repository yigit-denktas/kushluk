# Roadmap

Kuşluk uses iterative vertical slices rather than a long waterfall build.

## Stage 0 — Define the product

Goal: preserve intent before implementation.

Deliverables:
- Product
- Requirements
- Architecture
- Editorial System
- Design Brief
- Data Map
- Failure Matrix
- ADRs
- Stage 1 backlog
- Third-party reuse policy

Definition of Done:
A future maintainer/orchestrator can explain what Kuşluk is, what it is not, the non-negotiable decisions, and the next executable slice without relying on the founding conversation.

## Stage 1 — Walking skeleton

Goal: print one real edition end to end.

Minimum path:
- Köln/default weather;
- calendar fixture, then real calendar;
- three real public stories from a simple open source/RSS path;
- optional X/Grok experiment behind a connector seam;
- canonical candidate model;
- inspectable ranking;
- publication Markdown/metadata;
- deterministic A4 HTML;
- PDF validation;
- CUPS printing;
- digital fallback;
- archive.

Definition of Done:
One command produces a real morning edition with no manual HTML editing, and the system successfully produces multiple test editions.

## Stage 2 — Understand the day

Add:
- real calendar/task intelligence;
- robust travel-state detection;
- travel-aware destination weather;
- email fallback;
- pause/snooze controls;
- better printer state checks;
- typed failure notifications.

Definition of Done:
The system makes correct print-vs-digital decisions for normal home and travel scenarios and degrades cleanly when key context is missing.

## Stage 3 — Understand the user

Add:
- durable provider-independent interest model;
- connected newsletters;
- RSS bundles;
- X/social connector;
- Reddit/Hacker News;
- lightweight feedback;
- passive privacy-preserving learning.

Definition of Done:
Two materially different user profiles produce meaningfully different editions without recurring manual curation.

## Stage 3.5 — Editorial intelligence

Add:
- better clustering;
- source diversity;
- claim verification;
- continuity across editions;
- story threads;
- stronger serendipity;
- user-controlled editorial modes.

Definition of Done:
The edition routinely demonstrates useful synthesis rather than feed aggregation.

## Stage 4 — Physical and visual product

Add:
- production design system;
- paper profiles;
- monochrome/colour modes;
- printer compatibility testing;
- refined typography;
- editorial illustration;
- accessibility and print legibility testing.

Definition of Done:
A run of editions looks unmistakably like the same publication across supported printers/paper profiles.

## Stage 5 — Productise

Add:
- onboarding/configuration;
- install packaging;
- connector setup;
- self-hosting docs;
- e-reader surface;
- optional messaging;
- plugin/extension model;
- contributor docs.

Managed cloud, if pursued, receives its own privacy/security/product track.

Definition of Done:
A new user can install Kuşluk, connect supported services, and produce an edition without editing source code.

## Open investigations

- exact X/Grok Bot capabilities, costs, and reliability;
- upstream permissively licensed print-briefing projects;
- home-printer paper stocks and supported grammage;
- long-term printer upgrade path, especially monochrome laser/duplex;
- exact newsletter ingestion strategy;
- delivery channels beyond email;
- e-reader packaging;
- motion/animated digital edition semantics.
