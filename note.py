class Note:
    """Classe que representa uma nota individual."""
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def to_dict(self):
        """Converte a nota para um dicionário."""
        return {"title": self.title, "content": self.content}

    @staticmethod
    def from_dict(data):
        """Cria uma nota a partir de um dicionário."""
        return Note(data["title"], data["content"])