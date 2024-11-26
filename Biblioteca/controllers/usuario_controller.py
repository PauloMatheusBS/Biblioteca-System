from database.db_connection import DBConnection

class UsuarioController:
    def __init__(self, db_connection):
        self.conn = db_connection.get_conn()

    def cadastrar_usuario(self, usuario):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO Usuarios (nome, email, senha, cpf, admin) 
            VALUES (%s, %s, %s, %s, %s)
        """, (usuario.nome, usuario.email, usuario.senha, usuario.cpf, usuario.admin))
        self.conn.commit()
        cursor.close()

    def consultar_usuarios(self, filtro=None):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM Usuarios"
        if filtro:
            query += " WHERE nome LIKE %s OR email LIKE %s"
            cursor.execute(query, (f"%{filtro}%", f"%{filtro}%"))
        else:
            cursor.execute(query)
        usuarios = cursor.fetchall()
        cursor.close()
        return usuarios

    def atualizar_usuario(self, usuario_id, campos):
        cursor = self.conn.cursor()
        sets = ", ".join([f"{campo}=%s" for campo in campos.keys()])
        valores = list(campos.values()) + [usuario_id]
        cursor.execute(f"UPDATE Usuarios SET {sets} WHERE id=%s", valores)
        self.conn.commit()
        cursor.close()

    def excluir_usuario(self, usuario_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE id=%s", (usuario_id,))
        self.conn.commit()
        cursor.close()

