# ADR 0002 — One DIN A4 sheet by default

**Status:** Superseded by ADR 0013

## Context

The product is intended to be finite, readable, and easy to finish rather than an infinite feed.

## Decision

The default physical edition is one DIN A4 sheet. Duplex is preferred where hardware supports it; single-sided fallback is valid.

Extended/multi-page editions may exist later, but are not the default.

## Rationale

A bounded artifact improves attention, physical usability, and editorial discipline.

## Consequences

The editorial system must cut content to fit rather than continuously expanding the edition.

## Supersession

ADR 0013 replaces the one-sheet default with four logical A4 pages and separates editorial geometry from A4/A3 physical print profiles. The original bounded-artifact rationale remains valid.
