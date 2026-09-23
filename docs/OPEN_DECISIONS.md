# Open Decisions

Only decisions that materially change product direction belong here.
Implementation should continue around them when possible.

## 1. Canonical physical format

Current accepted ADR 0002 says the default physical edition is one DIN A4 sheet, preferably duplex.

Recent visual exploration introduced a second concept: one A3 landscape sheet (420 × 297 mm) with a 105 / 210 / 105 mm gatefold that closes to A4.

No implementation work needs to stop: Stage 1 remains A4 because that is the accepted architecture decision.

Decision needed later:
- keep A4 duplex as the canonical/default edition and treat A3 gatefold as an extended format; or
- supersede ADR 0002 and make the A3 gatefold the canonical format.

## 2. Final production typefaces

Playfair Display + Inter are safe prototype choices for layout development.
The final brand typefaces can be chosen later after print tests and licensing review.

This does not block Stage 1.
