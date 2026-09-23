# Design Brief

## Working direction: Warm Editorial Computing

Kuşluk should feel like a small publication made by a thoughtful editor, not a SaaS dashboard printed on paper.

The central tension is:

**digital intelligence → editorial judgment → physical object**

Technology should disappear into editorial craft. The final object should feel finite, calm, warm, tactile, literate, and contemporary.

## Identity

The primary identity is the exact wordmark:

**Kuşluk**

Use capital **K** followed by lowercase **uşluk**. Preserve the Turkish **ş**. Do not make all-caps `KUŞLUK` the primary masthead.

The wordmark should use a high-contrast editorial serif with:
- a strong capital K;
- compact editorial proportions;
- enough stroke robustness for inexpensive home printing;
- literary rather than luxury-fashion character.

The production typeface is not yet locked. Prototype layouts may use Playfair Display as a stand-in.

## Bird + sun

Bird and sun are recurring editorial motifs, not a compulsory corporate logo lockup.

- bird: observation, morning, messages, curiosity;
- sun: morning, warmth, cycle.

Use them sparsely. The wordmark must work alone. Do not repeat a bird/yellow-circle badge in every module.

## Palette

Material-first prototype palette:

- Paper Cream — `#F3EFE4`
- Soft Salmon — `#E8C9B8`
- Morning Yellow — `#F3D77B`
- Warm Grey — `#9A958D`
- Ink Black — `#1A1A1A`

Colour should often come from paper stock or a restrained spot-like accent rather than full-page ink coverage.

The system must remain legible in monochrome.

## References

The design may learn from:
- **Le Monde** — compositional discipline and calm editorial hierarchy;
- **Financial Times** — material/paper as part of identity;
- **The Guardian** — restrained moments of energy and editorial confidence;
- **Daylight Computer** — warm, tactile, anti-glare, non-sci-fi digital sensibility;
- contemporary tactile/analogue technology branding — used critically, not as lifestyle cosplay;
- independent literary publications and European editorial identity systems.

These are references, not templates to copy.

## Desired feeling

- warm;
- literate;
- tactile;
- contemporary;
- observant;
- slightly idiosyncratic;
- calm enough to read at breakfast;
- designed, but not precious;
- physical without fake vintage affectation.

## Avoid

- glassmorphism;
- neon AI gradients;
- glowing brains;
- cyberpunk motifs;
- generic rounded SaaS cards;
- dashboard density;
- tiny text to force fit;
- fake newsprint distress;
- ornamental nostalgia;
- giant repeated bird/sun badges;
- thick newspaper-stack mockups;
- lifestyle-mockup dominance.

## Typography

Use a serif-led editorial system.

Prototype relationship:
- expressive high-contrast serif for masthead and major headlines;
- highly legible quiet sans for body/utility/metadata where appropriate;
- optional restrained monospace only for identifiers and technical micro-data.

Prototype fonts may use Playfair Display + Inter; final production fonts require later print and licensing review.

Typography should survive inexpensive home printers.

## Layout

Start from newspaper/magazine composition rather than a component-card UI.

Use:
- a rigorous underlying column grid;
- thin rules;
- variable headline scale;
- asymmetry in moderation;
- active negative space;
- restrained photography/illustration;
- small uppercase metadata.

The page should feel composed by an editor, not assembled from dashboard cards.

Front side:
- calm;
- strong orientation;
- immediate scan of the day;
- no forced hero story.

Back side:
- more editorial;
- room for stories, language material, illustration, and curiosity.

## Physical object

The current accepted product decision remains one DIN A4 sheet, preferably duplex.

Recent design exploration also established a technically plausible A3 landscape gatefold:
- open: 420 × 297 mm;
- left flap: 105 mm;
- centre: 210 mm;
- right flap: 105 mm;
- closed: 210 × 297 mm (A4).

The A3 gatefold is **experimental until the physical-format decision is resolved** in `OPEN_DECISIONS.md`. Do not silently replace the accepted A4 default.

In all mockups, represent Kuşluk as a single thin sheet. No book spine, thick paper block, bound magazine, or newspaper bundle.

## Paper as a design token

Potential home-printable profiles:
- standard white;
- warm white / cream;
- recycled grey;
- pale yellow;
- pale pink / salmon;
- pale orange.

Prefer uncoated, matte, slightly fibrous stock. Real paper variation is welcome; fake vintage texture is not.

The printer is not assumed to detect paper colour or stock automatically.

## Imagery and illustration

Photography should be observational rather than advertising-like:
- streets;
- architecture;
- public transport;
- neighbourhood life;
- people at a distance;
- landscapes;
- objects;
- maps.

Preferred illustration vocabulary:
- small editorial line drawings;
- natural-history-like bird studies;
- diagrams;
- maps;
- restrained collage;
- halftone;
- simple iconography.

Do not rely on photoreal AI imagery as the default aesthetic.

## Edition identity and digital escape hatches

Edition identity should be stable and collectible, for example:

`20 SEP 2026 · EDITION 0042`

Machine/archive identity:

`20260920-042`

QR codes are functional escape hatches for deeper/live material, not decoration. Keep them small and attributable.

## Prototype guidance

Use generative visual tools to explore directions, but freeze approved layouts into deterministic HTML/CSS/SVG templates.

Daily generation must fill a design system; it must not redesign the publication from scratch each morning.
