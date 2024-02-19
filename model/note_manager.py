import json

from datetime import datetime
from model.note import Note


class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []

    def load_notes(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                loaded_notes = json.load(file)
                if loaded_notes:
                    for note_dict in loaded_notes:
                        note = Note(note_dict["title"], note_dict["body"])
                        note.created_at = datetime.fromisoformat(note_dict["created_at"])
                        note.updated_at = datetime.fromisoformat(note_dict["updated_at"])
                        self.notes.append(note)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass

    def save_notes(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([note.to_dict() for note in self.notes], file, ensure_ascii=False)

    def add_note(self, note):
        self.notes.append(note)

    def delete_note_by_id(self, id):
        self.notes = [note for note in self.notes if note.id != id]

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note

    def update_note_by_id(self, id, title, body):
        note = self.get_note_by_id(id)
        if note:
            note.update(title, body)

    def filter_notes_by_date(self, date):
        return [note for note in self.notes if note.created_at.date() == date]
