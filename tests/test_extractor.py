import os
import pytest
from slidenotes.extractor import extract

FIXTURE_PDF = os.path.join(os.path.dirname(__file__), "fixture.pdf")


def test_extract_returns_string():
    result = extract(FIXTURE_PDF)
    assert isinstance(result, str)


def test_extract_contains_text():
    result = extract(FIXTURE_PDF)
    assert "NLP" in result or len(result) > 0


def test_extract_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        extract("nonexistent.pdf")
