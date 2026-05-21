import sqlite3

class Usuario:
    def __init__(self, db_path="sigta.db"):
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                contrasena TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def validar(self, usuario, contrasena):
        self.cursor.execute(
            "SELECT * FROM usuarios WHERE usuario=? AND contrasena=?",
            (usuario, contrasena)
        )
        return self.cursor.fetchone() is not None

    def agregar_usuario(self, usuario, contrasena):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)",
                (usuario, contrasena)
            )
            self.conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def cerrar(self):
        self.conexion.close()