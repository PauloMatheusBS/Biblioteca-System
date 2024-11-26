from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QHBoxLayout, QMessageBox
from controllers.usuario_controller import UsuarioController

class GerenciarUsuariosWindow(QMainWindow):
    def __init__(self, db_connection):
        super().__init__()
        self.setWindowTitle("Gerenciar Usuários")
        self.db_connection = db_connection
        self.controller = UsuarioController(self.db_connection)

        layout = QVBoxLayout()

        self.filtro_input = QLineEdit()
        self.filtro_input.setPlaceholderText("Pesquisar usuário por nome ou email...")
        btn_pesquisar = QPushButton("Pesquisar")
        btn_pesquisar.clicked.connect(self.consultar_usuarios)

        # Botões para Adicionar, Atualizar e Excluir
        btn_adicionar = QPushButton("Adicionar Usuário")
        btn_adicionar.clicked.connect(self.adicionar_usuario)

        btn_atualizar = QPushButton("Atualizar Usuário")
        btn_atualizar.clicked.connect(self.atualizar_usuario)

        btn_excluir = QPushButton("Excluir Usuário")
        btn_excluir.clicked.connect(self.excluir_usuario)

        # Tabela para exibir os usuários
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Nome", "Email", "CPF", "Admin"])

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

    def consultar_usuarios(self):
        filtro = self.filtro_input.text()
        usuarios = self.controller.consultar_usuarios(filtro)
        self.table.setRowCount(len(usuarios))
        for row, usuario in enumerate(usuarios):
            self.table.setItem(row, 0, QTableWidgetItem(str(usuario['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(usuario['nome']))
            self.table.setItem(row, 2, QTableWidgetItem(usuario['email']))
            self.table.setItem(row, 3, QTableWidgetItem(usuario['cpf']))
            self.table.setItem(row, 4, QTableWidgetItem("Sim" if usuario['admin'] else "Não"))

    def adicionar_usuario(self):
        # Lógica para adicionar um novo usuário
        print("Abrir tela para adicionar um novo usuário.")

    def atualizar_usuario(self):
        # Lógica para atualizar um usuário selecionado
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            usuario_id = self.table.item(selected_row, 0).text()
            # Lógica para carregar as informações e permitir a edição
            print(f"Abrir tela para editar o usuário com ID: {usuario_id}")
        else:
            self.show_message("Erro", "Selecione um usuário para atualizar.")

    def excluir_usuario(self):
        # Lógica para excluir um usuário selecionado
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            usuario_id = self.table.item(selected_row, 0).text()
            usuario_nome = self.table.item(selected_row, 1).text()
            confirm = QMessageBox.question(self, "Confirmar Exclusão", 
                                           f"Você tem certeza que deseja excluir o usuário: {usuario_nome}?", 
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                # Excluir usuário
                self.controller.excluir_usuario(usuario_id)
                self.consultar_usuarios()  # Recarregar a lista de usuários
        else:
            self.show_message("Erro", "Selecione um usuário para excluir.")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()
