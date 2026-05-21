import sqlite3


conexion = sqlite3.connect("sigta.db")
cursor = conexion.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    contrasena TEXT NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    materia TEXT NOT NULL,
    fecha_entrega TEXT NOT NULL,
    estado TEXT NOT NULL,
    prioridad TEXT NOT NULL
)
""")


cursor.execute("""
INSERT OR IGNORE INTO usuarios (usuario, contrasena) 
VALUES ('admin', '1234')
""")


conexion.commit()
conexion.close()

print("Base de datos y tablas creadas correctamente")