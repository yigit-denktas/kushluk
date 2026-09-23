# Roadmap

Kuşluk uses iterative vertical slices rather than a long waterfall build.

## Stage 0 — Define the product

Status: **implementation-ready**

Goal: preserve intent before implementation.

Deliverables:
- Product
- Requirements
- Architecture
- Editorial System
- Design Brief
- Data Map
- Onboarding
- Failure Matrix
- ADRs
- Stage 1 backlog
- Third-party reuse policy
- Open-decisions register

Definition of Done:
A future maintainer/orchestrator can explain what Kuşluk is, what it is not, the non-negotiable decisions, and the next executable slice without relying on the founding conversation.

## Stage 1 — Walking skeleton

Status: **ACTIVE — software path exists; real local proof pending**

Goal: print one real edition end to end.

Implemented path:
- Köln/default weather;
- generic ICS calendar with fixture fallback;
- real RSS/Atom stories;
- canonical candidate and story-cluster models;
- inspectable deterministic ranking;
- publication Markdown/metadata;
- deterministic A4 HTML;
- PDF page validation and editorial cut/retry;
- CUPS capability detection and printing;
- SMTP digital delivery/fallback;
- archive and run summary;
- runtime doctor;
- CI smoke test.

Remaining proof:
- configure a real private calendar/task source;
- run on the chosen local host;
- reach the real printer;
- complete at least five real editions;
- tune from observed failures/read behaviour.

Definition of Done:
One command produces a real morning edition with no manual HTML editing, the local print/digital path works in the actual environment, and multiple real editions have been completed.

## Stage 2 — Understand the day

Add:
- richer calendar/task intelligence;
- robust travel-state detection;
- travel-aware destination weather;
- pause/snooze controls;
- stronger device-specific printer-state handling;
- user-facing typed failure notifications.

Definition of Done:
The system makes correct print-vs-digital decisions for normal home and travel scenarios and degrades cleanly when key context is missing.

## Stage 3 — Understand the user

Add:
- durable provider-independent interest model;
- newsletter discovery from a bounded connected-mailbox window;
- per-newsletter source modes: ignore, reference/source, derivative, private direct inclusion;
- connected newsletters;
- RSS bundles;
- X/social connector;
- Reddit/Hacker News;
- lightweight feedback;
- passive privacy-preserving learning.

Definition of Done:
Two materially different user profiles produce meaningfully different editions without recurring manual curation, and an existing newsletter diet can be converted into explicit source configuration without manually entering every subscription.

## Stage 3.5 — Editorial intelligence

Add:
- richer clustering/source diversity;
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
- newsletter discovery/review UI;
- install packaging;
- connector setup;
- self-hosting docs;
- e-reader surface;
- optional messaging;
- plugin/extension model;
- contributor docs.

Managed cloud, if pursued, receives its own privacy/security/product track.

Definition of Done:
A new user can install Kuşluk, connect supported services, review discovered sources, and produce an edition without editing source code.

## Open investigations

- exact X/Grok Bot capabilities, costs, and reliability;
- home-printer paper stocks and supported grammage;
- long-term printer upgrade path, especially monochrome laser/duplex;
- newsletter detection precision and provider-specific mail APIs;
- delivery channels beyond email;
- e-reader packaging;
- motion/animated digital edition semantics.
