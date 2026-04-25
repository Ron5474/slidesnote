import os
import pytest
from unittest.mock import patch
from slidenotes.slidenotes import main

FIXTURE_PDF = os.path.join(os.path.dirname(__file__), "fixture.pdf")


def test_main_generates_notes_file(tmp_path):
    pdf_path = tmp_path / "lecture.pdf"
    import shutil
    shutil.copy(FIXTURE_PDF, pdf_path)

    with patch("slidenotes.slidenotes.generate", return_value="# Generated Notes\n- Point 1"):
        main([str(pdf_path)])

    notes_path = tmp_path / "lecture_notes.md"
    assert notes_path.exists()
    assert "Generated Notes" in notes_path.read_text()


def test_main_skips_if_notes_exist(tmp_path, capsys):
    pdf_path = tmp_path / "lecture.pdf"
    notes_path = tmp_path / "lecture_notes.md"
    import shutil
    shutil.copy(FIXTURE_PDF, pdf_path)
    notes_path.write_text("existing notes")

    with patch("slidenotes.slidenotes.generate") as mock_gen:
        main([str(pdf_path)])
        mock_gen.assert_not_called()

    captured = capsys.readouterr()
    assert "already exist" in captured.out


def test_main_errors_on_missing_pdf(capsys):
    with pytest.raises(SystemExit) as exc_info:
        main(["nonexistent.pdf"])
    assert exc_info.value.code != 0
    captured = capsys.readouterr()
    assert "not found" in captured.out.lower() or "not found" in captured.err.lower()
