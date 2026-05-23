import json
import os

class Usuario:
    def __init__(self, db_path="usuarios.json"):
        self.db_path = db_path
        if not os.path.exists(db_path):
            with open(db_path, "w") as f:
                json.dump([], f)

    def agregar_usuario(self, nombre, contrasena):
        with open(self.db_path, "r") as f:
            usuarios = json.load(f)
        for u in usuarios:
            if u["nombre"] == nombre:
                return None
        usuario_id = len(usuarios) + 1
        usuarios.append({"id": usuario_id, "nombre": nombre, "contrasena": contrasena})
        with open(self.db_path, "w") as f:
            json.dump(usuarios, f)
        return usuario_id

    def validar(self, nombre, contrasena):
        with open(self.db_path, "r") as f:
            usuarios = json.load(f)
        for u in usuarios:
            if u["nombre"] == nombre and u["contrasena"] == contrasena:
                return u["id"]
        return None