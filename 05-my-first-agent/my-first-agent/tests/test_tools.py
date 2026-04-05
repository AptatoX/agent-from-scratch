from pathlib import Path

from tools import get_time, read_notes, save_note


def test_get_time_returns_text():
    result = get_time()
    assert isinstance(result, str)
    assert len(result) > 0


def test_save_note_and_read_notes(tmp_path):
    note_file = tmp_path / "notes.txt"

    save_result = save_note("learn agents", note_file)
    read_result = read_notes(note_file)

    assert "saved" in save_result.lower()
    assert "learn agents" in read_result


def test_read_notes_when_file_is_empty(tmp_path):
    note_file = tmp_path / "notes.txt"
    note_file.write_text("", encoding="utf-8")

    result = read_notes(note_file)

    assert "no notes" in result.lower()
