class Emprestimo:
    def __init__(self, id=None, usuario_id=None, livro_id=None, data_emprestimo=None, data_devolucao=None):
        self.id = id  # Identificador único
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def to_dict(self):
        """Converte o objeto Emprestimo em um dicionário."""
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "livro_id": self.livro_id,
            "data_emprestimo": self.data_emprestimo,
            "data_devolucao": self.data_devolucao,
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Emprestimo a partir de um dicionário."""
        return Emprestimo(
            id=data.get("id"),
            usuario_id=data.get("usuario_id"),
            livro_id=data.get("livro_id"),
            data_emprestimo=data.get("data_emprestimo"),
            data_devolucao=data.get("data_devolucao"),
        )

    def emprestimo_ativo(self):
        """Verifica se o empréstimo está ativo (sem data de devolução)."""
        return self.data_devolucao is None
