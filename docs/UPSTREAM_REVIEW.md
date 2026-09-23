# Upstream Review

This document records public projects reviewed as references before Kuşluk implementation.
No upstream code is copied into Kuşluk by this review.

## Firstlight — cruftbox/firstlight

License: MIT.

Useful patterns:
- Open-Meteo for keyless weather;
- standard RSS feeds for news;
- local Docker/home-server orientation;
- A4/single-page printing;
- archive and print controls.

Kuşluk decision:
Use the same general class of boring, replaceable infrastructure, but keep Kuşluk's canonical publication model and editorial layer independent.

## Morning Paper — dmthepm/morning-paper

License: MIT.

Useful patterns:
- private newsroom represented as owned files;
- CLI rendering to PDF;
- finite anti-feed framing;
- durable editorial/preferences files.

Kuşluk decision:
Reuse the separation of owned editorial state from rendering as a design reference, not as a hard dependency.

## OpenPaper — falense/openpaper

License: MIT.

Useful patterns:
- deterministic source fetchers;
- separate ingestion and curation stages;
- local source/cache/archive directories;
- explicit seen/deduplication state.

Kuşluk decision:
Adopt the connector boundary and deterministic fetch-before-curation principle. Do not copy its broadsheet product assumptions.

## Hermes Paper Agent — vaelkeep/hermes-paper-agent

License: verify exact repository license before copying any code.

Useful patterns:
- generator and print engine separated by a markdown publication contract;
- write → check → fix loop before publishing;
- provenance recorded per edition;
- fixtures that allow the pipeline to run before personal connectors are ready.

Kuşluk decision:
Adopt the publication-contract and validation-loop concepts. No code is incorporated by this review.

## Review result

Stage 1 can proceed without an upstream runtime dependency.

The selected implementation strategy is intentionally conventional:

`connectors -> canonical candidates -> ranking -> publication model -> deterministic HTML -> optional PDF -> print adapter -> archive`

This keeps upstream reuse available later at clear seams and avoids inheriting another project's product assumptions.
