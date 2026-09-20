# Product

## Product statement

Kuşluk is a local-first, print-first daily briefing system that creates a small personal newspaper rather than another dashboard.

Its job is to answer:

> **What is worth my attention this morning, given my actual day and my longer-term interests?**

The default artifact is one DIN A4 sheet, ideally printed front and back, designed for roughly 10–15 minutes of reading.

## Primary experience

By the configured morning deadline, default 08:00 local time:

- if the user is home and printing is healthy, produce the physical edition;
- if printing is unavailable, fail visibly and deliver the edition digitally;
- if the user is travelling, avoid wasting paper and deliver the edition digitally;
- adapt weather and relevant context to the travel destination when reliable context exists.

The front side is primarily **Today**: stable commitments and immediate orientation.

The back side is primarily **For You**: editorially selected stories, language material, personal columns, and serendipity.

## Why print

The product deliberately creates a bounded physical object:
- finite rather than infinite;
- editorial rather than feed-like;
- readable away from notification-heavy screens;
- easy to finish;
- physically memorable and archivable.

Digital surfaces exist to complement print, not to turn Kuşluk into another scrolling application.

## Personalisation

Personalisation should come from low-effort or passive signals:
- user-declared interests and beats;
- newsletters and RSS;
- optionally connected social sources such as X;
- calendar and tasks;
- historical editions and lightweight feedback;
- future privacy-preserving reading signals.

Recurring manual tagging, manual exports, or daily preference maintenance are not acceptable foundations.

### Recovering value from existing subscriptions

A user's inbox already contains editorial choices they made outside Kuşluk.

When email is explicitly connected, onboarding should help discover likely newsletters and recurring editorial mail, then ask the user how each source should participate in Kuşluk.

A newsletter may be:
- ignored;
- used only as a source/candidate signal;
- transformed into Kuşluk-native summaries or derivatives;
- included more directly in the user's private personal edition.

The purpose is not generic email summarisation. It is to recover value from newsletters the user already chose to receive but may not have time to read.

See `ONBOARDING.md` and ADR 0012.

## Editorial character

- factual core;
- conversational connective tissue;
- references to previous editions when useful;
- no obligation to manufacture a lead story;
- important world events may override narrow interest relevance;
- deliberate room for useful surprise.

## Language

Language is a user-level preference, not a fixed product choice.

An edition may:
- be entirely in one selected language;
- use different languages by section;
- intentionally mix languages within a section when that serves learning or tone.

Initial development should support English, German, and Turkish well, without hard-coding those as the only possible languages.

## Future surfaces

Planned, but not MVP:
- e-reader/e-ink editions;
- richer HTML edition;
- animated editorial stories for capable digital displays;
- multi-page or extended editions;
- messaging delivery;
- optional managed-cloud deployment.

## Non-goals

Kuşluk is not:
- a generic autonomous-agent framework;
- a replacement for live travel apps;
- a social network;
- an infinite news feed;
- a surveillance/analytics platform;
- a central behavioural-data business;
- a dashboard that requires the user to sit at a computer.

## Product Definition of Done

A mature Kuşluk installation should reliably:
1. understand the day's stable commitments;
2. gather a broad but controlled candidate pool;
3. select rather than merely aggregate;
4. produce an attractive bounded edition by the configured deadline;
5. print when appropriate and fall back digitally when not;
6. explain material failures;
7. preserve a durable edition archive;
8. keep personal data under user control by default.
