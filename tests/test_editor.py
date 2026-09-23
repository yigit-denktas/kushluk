from kushluk.editor import cluster_candidates, select_stories
from kushluk.models import Candidate, SourceRef


def candidate(title: str, score_seed: float, url: str, source="Test") -> Candidate:
    return Candidate(
        id=url,
        title=title,
        summary="Summary",
        source=SourceRef(kind="rss", name=source),
        url=url,
        relevance=score_seed,
        importance=score_seed,
        freshness=score_seed,
        novelty=score_seed,
    )


def test_select_stories_ranks_and_clusters_duplicates():
    stories = select_stories(
        [
            candidate("Same Story About AI", 0.4, "https://a.test/story", "A"),
            candidate("Same Story About AI!", 0.9, "https://b.test/story", "B"),
            candidate("Another Story", 0.8, "https://c.test/story", "C"),
        ],
        limit=3,
    )
    assert len(stories) == 2
    assert stories[0].headline == "Same Story About AI!"
    assert stories[0].cluster_size == 2
    assert "score" in stories[0].why_selected


def test_same_url_clusters_even_if_query_strings_differ():
    clusters = cluster_candidates(
        [
            candidate("Title one", 0.5, "https://example.com/a?utm_source=x"),
            candidate("Different title", 0.6, "https://example.com/a?ref=y"),
        ]
    )
    assert len(clusters) == 1
