"""
Interface de Linha de Comando para gerenciar notas.
"""
from note_manager import NoteManager

class CLI:
    """Interface de Linha de Comando para gerenciar notas."""
    def __init__(self):
        self.manager = NoteManager()

    def run(self):
        """Inicia o aplicativo CLI."""
        while True:
            print("\nGerenciador de Notas")
            print("1. Criar uma nota")
            print("2. Editar uma nota")
            print("3. Buscar uma nota")
            print("4. Listar todas as notas")
            print("5. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self._create_note()
            elif choice == "2":
                self._edit_note()
            elif choice == "3":
                self._search_note()
            elif choice == "4":
                self._list_notes()
            elif choice == "5":
                print("Saindo do Gerenciador de Notas. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def _create_note(self):
        title = input("Título da nota: ")
        content = input("Conteúdo da nota: ")
        self.manager.create_note(title, content)
        print("Nota criada com sucesso!")

    def _edit_note(self):
        title = input("Título da nota que deseja editar: ")
        new_content = input("Novo conteúdo: ")
        try:
            self.manager.edit_note(title, new_content)
            print("Nota editada com sucesso!")
        except ValueError as e:
            print(e)

    def _search_note(self):
        title = input("Título da nota que deseja buscar: ")
        try:
            note = self.manager.search_note(title)
            print(f"\nTítulo: {note.title}\nConteúdo: {note.content}")
        except ValueError as e:
            print(e)

    def _list_notes(self):
        notes = self.manager.list_notes()
        if not notes:
            print("Nenhuma nota encontrada.")
        else:
            for note in notes:
                print(f"- {note.title}")


if __name__ == "__main__":
    CLI().run()
