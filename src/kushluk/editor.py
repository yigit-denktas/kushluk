from __future__ import annotations

from collections import OrderedDict

from kushluk.models import Candidate, Story


def select_stories(candidates: list[Candidate], limit: int = 3) -> list[Story]:
    """Deduplicate by normalized title, rank, and expose why each story was selected."""
    unique: OrderedDict[str, Candidate] = OrderedDict()
    for candidate in sorted(candidates, key=lambda item: item.score, reverse=True):
        key = _title_key(candidate.title)
        if key and key not in unique:
            unique[key] = candidate

    stories: list[Story] = []
    for candidate in list(unique.values())[:limit]:
        stories.append(
            Story(
                id=candidate.id,
                headline=candidate.title,
                deck=candidate.summary or "Open the source for the full story.",
                source_name=candidate.source.name,
                source_url=candidate.url or candidate.source.url,
                why_selected=(
                    f"score {candidate.score:.2f}: relevance {candidate.relevance:.2f}, "
                    f"importance {candidate.importance:.2f}, freshness {candidate.freshness:.2f}, "
                    f"novelty {candidate.novelty:.2f}"
                ),
            )
        )
    return stories


def _title_key(title: str) -> str:
    return " ".join("".join(ch.lower() if ch.isalnum() else " " for ch in title).split())
