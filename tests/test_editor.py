from kushluk.editor import select_stories
from kushluk.models import Candidate, SourceRef


def candidate(title: str, score_seed: float, url: str) -> Candidate:
    return Candidate(
        id=url,
        title=title,
        summary="Summary",
        source=SourceRef(kind="rss", name="Test"),
        url=url,
        relevance=score_seed,
        importance=score_seed,
        freshness=score_seed,
        novelty=score_seed,
    )


def test_select_stories_ranks_and_deduplicates():
    stories = select_stories(
        [
            candidate("Same Story", 0.4, "a"),
            candidate("same-story!", 0.9, "b"),
            candidate("Another Story", 0.8, "c"),
        ],
        limit=3,
    )
    assert [story.id for story in stories] == ["b", "c"]
    assert "score" in stories[0].why_selected
