from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QTableWidget, QTableWidgetItem, QLineEdit, QHBoxLayout, QMessageBox
from controllers.emprestimo_controller import EmprestimoController

class GerenciarEmprestimosWindow(QMainWindow):
    def __init__(self, db_connection):
        super().__init__()
        self.setWindowTitle("Gerenciar Empréstimos")
        self.db_connection = db_connection
        self.controller = EmprestimoController(self.db_connection)

        layout = QVBoxLayout()

        # Filtro de pesquisa
        self.filtro_input = QLineEdit()
        self.filtro_input.setPlaceholderText("Pesquisar empréstimos por usuário ou livro...")
        btn_pesquisar = QPushButton("Pesquisar")
        btn_pesquisar.clicked.connect(self.consultar_emprestimos)

        # Tabela de empréstimos
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Usuário", "Livro", "Data Empréstimo", "Data Devolução"])

        # Botões de ação
        btn_realizar = QPushButton("Realizar Empréstimo")
        btn_realizar.clicked.connect(self.realizar_emprestimo)

        btn_devolver = QPushButton("Devolver Empréstimo")
        btn_devolver.clicked.connect(self.devolver_emprestimo)

        # Layout dos componentes
        layout.addWidget(self.filtro_input)
        layout.addWidget(btn_pesquisar)
        layout.addWidget(self.table)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(btn_realizar)
        buttons_layout.addWidget(btn_devolver)

        layout.addLayout(buttons_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def consultar_emprestimos(self):
        filtro = self.filtro_input.text()
        emprestimos = self.controller.consultar_emprestimos(filtro)
        self.table.setRowCount(len(emprestimos))
        for row, emprestimo in enumerate(emprestimos):
            self.table.setItem(row, 0, QTableWidgetItem(str(emprestimo['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(emprestimo['usuario']))
            self.table.setItem(row, 2, QTableWidgetItem(emprestimo['livro']))
            self.table.setItem(row, 3, QTableWidgetItem(emprestimo['data_emprestimo']))
            self.table.setItem(row, 4, QTableWidgetItem(emprestimo['data_devolucao'] if emprestimo['data_devolucao'] else "Não devolvido"))

    def realizar_emprestimo(self):
        # Aqui você pode abrir uma nova tela/formulário para realizar o empréstimo
        print("Abrir tela para realizar empréstimo.")

    def devolver_emprestimo(self):
        # Lógica para devolver um empréstimo
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            emprestimo_id = self.table.item(selected_row, 0).text()
            # Confirmar devolução
            confirm = QMessageBox.question(self, "Confirmar Devolução", 
                                           f"Você tem certeza que deseja devolver o empréstimo ID: {emprestimo_id}?", 
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                # Chamar método para devolver empréstimo
                self.controller.devolver_emprestimo(emprestimo_id)
                self.consultar_emprestimos()  # Atualizar a lista de empréstimos
        else:
            self.show_message("Erro", "Selecione um empréstimo para devolver.")

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()
