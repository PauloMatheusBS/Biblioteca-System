from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget
from views.gerenciar_livros import GerenciarLivrosWindow
from views.gerenciar_usuarios import GerenciarUsuariosWindow
from views.gerenciar_emprestimos import GerenciarEmprestimosWindow

class MainWindow(QMainWindow):
    def __init__(self, db_connection):
        super().__init__()
        self.setWindowTitle("Sistema de Gerenciamento de Biblioteca")
        self.db_connection = db_connection

        layout = QVBoxLayout()

        # Botões para cada seção
        btn_livros = QPushButton("Gerenciar Livros")
        btn_livros.clicked.connect(self.abrir_gerenciar_livros)

        btn_usuarios = QPushButton("Gerenciar Usuários")
        btn_usuarios.clicked.connect(self.abrir_gerenciar_usuarios)

        btn_emprestimos = QPushButton("Gerenciar Empréstimos")
        btn_emprestimos.clicked.connect(self.abrir_gerenciar_emprestimos)

        layout.addWidget(btn_livros)
        layout.addWidget(btn_usuarios)
        layout.addWidget(btn_emprestimos)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Métodos para abrir as janelas específicas
    def abrir_gerenciar_livros(self):
        self.livros_window = GerenciarLivrosWindow(self.db_connection)
        self.livros_window.show()

    def abrir_gerenciar_usuarios(self):
        self.usuarios_window = GerenciarUsuariosWindow(self.db_connection)
        self.usuarios_window.show()

    def abrir_gerenciar_emprestimos(self):
        self.emprestimos_window = GerenciarEmprestimosWindow(self.db_connection)
        self.emprestimos_window.show()
