import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow
from database.db_connection import DBConnection

def main():
    # Estabelecendo a conexão com o banco de dados
    db_connection = DBConnection().connect()

    # Inicializando a aplicação Qt
    app = QApplication(sys.argv)

    # Criando e mostrando a janela principal
    main_window = MainWindow(db_connection)
    main_window.show()

    # Executando a aplicação Qt
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
