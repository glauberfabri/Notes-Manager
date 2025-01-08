"""
Gerencia operações de criar, editar, buscar e salvar notas.
"""
import json
from typing import List
from note import Note

class NoteManager:
    """Classe que gerencia as operações de notas."""
    def __init__(self, filename: str = "notes.json"):
        self.filename = filename
        self.notes: List[Note] = []
        self._load_notes()

    def _load_notes(self):
        """Carrega as notas salvas do arquivo."""
        try:
            with open(self.filename, "r") as file:
                notes_data = json.load(file)
                self.notes = [Note.from_dict(note) for note in notes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.notes = []

    def _save_notes(self):
        """Salva as notas no arquivo."""
        with open(self.filename, "w") as file:
            json.dump([note.to_dict() for note in self.notes], file, indent=4)

    def create_note(self, title: str, content: str):
        """Cria uma nova nota."""
        self.notes.append(Note(title, content))
        self._save_notes()

    def edit_note(self, title: str, new_content: str):
        """Edita o conteúdo de uma nota existente."""
        for note in self.notes:
            if note.title == title:
                note.content = new_content
                self._save_notes()
                return
        raise ValueError(f"Nota com título '{title}' não encontrada.")

    def search_note(self, title: str) -> Note:
        """Busca uma nota pelo título."""
        for note in self.notes:
            if note.title == title:
                return note
        raise ValueError(f"Nota com título '{title}' não encontrada.")

    def list_notes(self):
        """Lista todas as notas."""
        return self.notes