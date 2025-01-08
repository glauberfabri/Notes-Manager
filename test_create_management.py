import pytest
from note_manager import NoteManager

def test_create_note():
    manager = NoteManager(filename="test_notes.json")
    manager.create_note("Teste", "Conteúdo de Teste")
    assert any(note.title == "Teste" for note in manager.list_notes())

def test_edit_note():
    manager = NoteManager(filename="test_notes.json")
    manager.create_note("Teste", "Conteúdo de Teste")
    manager.edit_note("Teste", "Conteúdo Atualizado")
    assert manager.search_note("Teste").content == "Conteúdo Atualizado"

def test_search_note():
    manager = NoteManager(filename="test_notes.json")
    manager.create_note("Teste", "Conteúdo de Teste")
    note = manager.search_note("Teste")
    assert note.title == "Teste"
    assert note.content == "Conteúdo de Teste"

def test_list_notes():
    manager = NoteManager(filename="test_notes.json")
    manager.create_note("Teste", "Conteúdo de Teste")
    notes = manager.list_notes()
    assert len(notes) > 0

def test_note_not_found():
    manager = NoteManager(filename="test_notes.json")
    with pytest.raises(ValueError):
        manager.search_note("Inexistente")
