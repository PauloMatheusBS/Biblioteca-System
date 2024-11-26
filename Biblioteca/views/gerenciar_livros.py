from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QHBoxLayout, QMessageBox
from controllers.livro_controller import LivroController

class GerenciarLivrosWindow(QMainWindow):
    def __init__(self, db_connection):
        super().__init__()
        self.setWindowTitle("Gerenciar Livros")
        self.db_connection = db_connection
        self.controller = LivroController(self.db_connection)

        layout = QVBoxLayout()

        self.filtro_input = QLineEdit()
        self.filtro_input.setPlaceholderText("Pesquisar livro...")
        btn_pesquisar = QPushButton("Pesquisar")
        btn_pesquisar.clicked.connect(self.consultar_livros)

        # Botões para Adicionar, Atualizar e Excluir
        btn_adicionar = QPushButton("Adicionar Livro")
        btn_adicionar.clicked.connect(self.adicionar_livro)

        btn_atualizar = QPushButton("Atualizar Livro")
        btn_atualizar.clicked.connect(self.atualizar_livro)

        btn_excluir = QPushButton("Excluir Livro")
        btn_excluir.clicked.connect(self.excluir_livro)

        # Tabela para exibir os livros
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Título", "Autor", "ISBN", "Gênero"])

        # Layout de botões
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(btn_adicionar)
        buttons_layout.addWidget(btn_atualizar)
        buttons_layout.addWidget(btn_excluir)

        layout.addWidget(self.filtro_input)
        layout.addWidget(btn_pesquisar)
        layout.addLayout(buttons_layout)
        layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def consultar_livros(self):
        filtro = self.filtro_input.text()
        livros = self.controller.consultar_livros(filtro)
        self.table.setRowCount(len(livros))
        for row, livro in enumerate(livros):
            self.table.setItem(row, 0, QTableWidgetItem(str(livro['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(livro['titulo']))
            self.table.setItem(row, 2, QTableWidgetItem(livro['autor']))
            self.table.setItem(row, 3, QTableWidgetItem(livro['isbn']))
            self.table.setItem(row, 4, QTableWidgetItem(livro['genero']))

    def adicionar_livro(self):
        # Lógica para adicionar um novo livro
        # Pode ser aberta uma nova tela de cadastro de livro
        print("Abrir tela para adicionar um novo livro.")

    def atualizar_livro(self):
        # Lógica para atualizar um livro selecionado
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            livro_id = self.table.item(selected_row, 0).text()
            # Lógica para carregar as informações e permitir a edição
            print(f"Abrir tela para editar o livro com ID: {livro_id}")
        else:
            self.show_message("Erro", "Selecione um livro para atualizar.")

    def excluir_livro(self):
        # Lógica para excluir um livro selecionado
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            livro_id = self.table.item(selected_row, 0).text()
            livro_title = self.table.item(selected_row, 1).text()
            confirm = QMessageBox.question(self, "Confirmar Exclusão", 
                                           f"Você tem certeza que deseja excluir o livro: {livro_title}?", 
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                # Excluir livro
                self.controller.excluir_livro(livro_id)
                self.consultar_livros()  # Recarregar a lista de livros
        else:
            self.show_message("Erro", "Selecione um livro para excluir.")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()
