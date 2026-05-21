import sqlite3
import pandas as pd

class VerTablas:
    def __init__(self, db_path="sigta.db"):
        self.db_path = db_path

    def mostrar_tabla(self, nombre_tabla):
        conexion = sqlite3.connect(self.db_path)
        try:
            df = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", conexion)
            print(f"\n=== Tabla {nombre_tabla} ===")
            print(df)
        except Exception as e:
            print(f"Error al mostrar la tabla {nombre_tabla}: {e}")
        finally:
            conexion.close()

    def mostrar_todas_las_tablas(self):
        conexion = sqlite3.connect(self.db_path)
        cursor = conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [t[0] for t in cursor.fetchall()]
        print("\nTablas disponibles en la base de datos:", tablas)
        for tabla in tablas:
            self.mostrar_tabla(tabla)
        conexion.close()


if __name__ == "__main__":
    vt = VerTablas()
    vt.mostrar_todas_las_tablas()