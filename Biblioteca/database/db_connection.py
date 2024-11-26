import mysql.connector

class DBConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão bem-sucedida ao banco de dados!")
            return self.connection
        except mysql.connector.Error as err:
            print(f"Erro de conexão: {err}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão fechada.")

