from database.db_connection import DBConnection

class EmprestimoController:
    def __init__(self, db_connection):
        self.conn = db_connection.get_conn()

    def realizar_emprestimo(self, usuario_id, livro_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Emprestimos (usuario_id, livro_id, data_emprestimo) 
            VALUES (%s, %s, CURDATE())
        """, (usuario_id, livro_id))
        cursor.execute("UPDATE Livros SET disponivel=FALSE WHERE id=%s", (livro_id,))
        self.conn.commit()
        cursor.close()

    def consultar_emprestimos(self, filtro=None):
        cursor = self.conn.cursor(dictionary=True)
        query = """
            SELECT E.id, U.nome AS usuario, L.titulo AS livro, E.data_emprestimo, E.data_devolucao
            FROM Emprestimos E
            JOIN Usuarios U ON E.usuario_id = U.id
            JOIN Livros L ON E.livro_id = L.id
        """
        if filtro:
            query += " WHERE U.nome LIKE %s OR L.titulo LIKE %s"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)
        emprestimos = cursor.fetchall()
        cursor.close()
        return emprestimos

    def devolver_emprestimo(self, emprestimo_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE Emprestimos SET data_devolucao=CURDATE() WHERE id=%s
        """, (emprestimo_id,))
        cursor.execute("""
            UPDATE Livros 
            SET disponivel=TRUE 
            WHERE id=(SELECT livro_id FROM Emprestimos WHERE id=%s)
        """, (emprestimo_id,))
        self.conn.commit()
        cursor.close()


