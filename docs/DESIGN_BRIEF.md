# Design Brief

## Working direction: Warm Editorial Computing

Kuşluk should feel like a small publication made by a thoughtful editor, not a SaaS dashboard printed on paper.

The design should combine:
- **Le Monde** — compositional discipline and calm editorial hierarchy;
- **Financial Times** — paper/material as part of identity;
- **The Guardian** — restrained moments of energy and editorial confidence;
- **Daylight Computer** — warm, tactile, anti-glare, non-sci-fi digital sensibility;
- contemporary AI brands' turn toward cafés, libraries, print ephemera, wood, paper, and analogue cues — used critically, not as lifestyle cosplay;
- the personal artifact quality of Karen X. Cheng's morning newspaper;
- the practical print discipline seen in existing morning-briefing skills.

These are references, not templates to copy.

## Desired feeling

- warm;
- literate;
- tactile;
- contemporary;
- slightly idiosyncratic;
- calm enough to read at breakfast;
- designed, but not precious;
- physical without fake vintage affectation.

## Avoid

- glassmorphism;
- neon AI gradients;
- glowing brains;
- cyberpunk motifs;
- generic rounded SaaS cards everywhere;
- dashboard density;
- tiny text to force fit;
- fake newsprint distress textures;
- ornamental nostalgia that reduces readability.

## Typography

Use editorial typography.

Preferred relationship:
- expressive but readable serif for editorial identity/headlines;
- highly legible serif or sans for body and utility information;
- restrained monospace only for identifiers, times, coordinates, technical micro-data where useful.

Typography should survive inexpensive home printers.

## Layout

Start from newspaper/magazine composition rather than component-grid UI.

Front side:
- calm;
- strong orientation;
- immediate scan of day;
- no forced hero story.

Back side:
- more playful;
- more editorial;
- room for personal columns, language, illustration, curiosity.

Whitespace is an active element.

## Paper as a design token

Paper may vary by user profile.

Potential home-printable profiles:
- standard white;
- warm white / cream;
- recycled grey;
- pale yellow;
- pale pink / salmon;
- pale orange.

The design system must maintain contrast across declared paper profiles.

The printer is not assumed to detect these profiles automatically.

## Colour

The design must work in:
- monochrome laser;
- black ink on coloured stock;
- colour inkjet.

Colour is optional enhancement, not a structural dependency.

## Illustration

Illustration/cartoon can be part of the publication identity.

Preferred visual vocabulary:
- small editorial line drawings;
- collage/cut-paper cues;
- diagrams;
- maps;
- restrained halftone;
- simple iconography.

Do not rely on photoreal AI imagery as the default aesthetic.

## Future digital surfaces

E-reader/e-ink:
- preserve editorial hierarchy;
- use high contrast;
- avoid interactions required for basic comprehension.

Animated "Daily Prophet"-like surfaces:
- a later digital enhancement;
- motion must add editorial meaning;
- static fallback is mandatory.

## Prototype guidance

Use generative visual tools to explore directions, but freeze approved layouts into deterministic HTML/CSS templates.

Daily generation must fill a design system; it must not redesign the newspaper from scratch each morning.
