from kushluk.printing import parse_lpoptions


def test_parse_lpoptions_detects_duplex_and_media():
    sample = """
Duplex/2-Sided Printing: *None DuplexNoTumble DuplexTumble
PageSize/Media Size: *A4 Letter A5
"""
    duplex, media = parse_lpoptions(sample)
    assert duplex is True
    assert "A4" in media


def test_parse_lpoptions_handles_simplex_printer():
    sample = "PageSize/Media Size: *A4 Letter\n"
    duplex, media = parse_lpoptions(sample)
    assert duplex is False
    assert media == ("A4", "Letter")
