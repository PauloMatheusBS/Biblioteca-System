class Usuario:
    def __init__(self, id=None, nome="", email="", senha="", cpf="", admin=False):
        self.id = id  # Identificador único
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.admin = admin

    def to_dict(self):
        """Converte o objeto Usuario em um dicionário."""
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "cpf": self.cpf,
            "admin": self.admin,
        }

    @staticmethod
    def from_dict(data):
        """Cria um objeto Usuario a partir de um dicionário."""
        return Usuario(
            id=data.get("id"),
            nome=data.get("nome"),
            email=data.get("email"),
            senha=data.get("senha"),
            cpf=data.get("cpf"),
            admin=data.get("admin", False),
        )

    @staticmethod
    def validar_email(email):
        """Valida o formato do email."""
        import re
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

    @staticmethod
    def validar_cpf(cpf):
        """Valida o formato do CPF (apenas tamanho e dígitos)."""
        return cpf.isdigit() and len(cpf) == 11

