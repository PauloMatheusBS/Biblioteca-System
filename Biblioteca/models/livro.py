class Livro:
    def __init__(self, id=None, titulo="", autor="", isbn="", genero="", disponivel=True):
        self.id = id  # Atributo opcional para identificar o livro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.disponivel = disponivel

    def to_dict(self):
        """Converte o objeto Livro em um dicionário."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "genero": self.genero,
            "disponivel": self.disponivel,
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Livro a partir de um dicionário."""
        return Livro(
            id=data.get("id"),
            titulo=data.get("titulo"),
            autor=data.get("autor"),
            isbn=data.get("isbn"),
            genero=data.get("genero"),
            disponivel=data.get("disponivel", True),
        )

