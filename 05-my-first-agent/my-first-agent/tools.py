from datetime import datetime
from pathlib import Path


def get_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_note(text, note_file=Path("notes.txt")):
    note_file = Path(note_file)
    cleaned_text = text.strip()
    with note_file.open("a", encoding="utf-8") as file:
        file.write(cleaned_text + "\n")
    return f"Saved note: {cleaned_text}"


def read_notes(note_file=Path("notes.txt")):
    note_file = Path(note_file)
    if not note_file.exists():
        return "No notes found yet."

    content = note_file.read_text(encoding="utf-8").strip()
    if not content:
        return "No notes found yet."

    return content
