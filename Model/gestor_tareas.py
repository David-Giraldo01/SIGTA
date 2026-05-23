from Model.tarea import Tarea
from Model.priorizador import Priorizador

import json
import os
from Model.tarea import Tarea

class GestorTareas:
    def __init__(self, db_path="tareas.json"):
        self.db_path = db_path
        if not os.path.exists(db_path):
            with open(db_path, "w") as f:
                json.dump([], f)

    def crear_tarea(self, usuario_id, nombre, descripcion, materia, fecha_entrega):
        with open(self.db_path, "r") as f:
            tareas = json.load(f)
        tarea_id = len(tareas) + 1
        tarea = Tarea(tarea_id, usuario_id, nombre, descripcion, materia, fecha_entrega)
        tareas.append({
            "id": tarea.id,
            "usuario_id": tarea.usuario_id,
            "nombre": tarea.nombre,
            "descripcion": tarea.descripcion,
            "materia": tarea.materia,
            "fecha_entrega": tarea.fecha_entrega,
            "estado": tarea.estado,
            "prioridad": tarea.prioridad
        })
        with open(self.db_path, "w") as f:
            json.dump(tareas, f)
        return tarea

    def listar_tareas(self, usuario_id):
        with open(self.db_path, "r") as f:
            tareas_json = json.load(f)
        tareas = []
        for f in tareas_json:
            if f["usuario_id"] == usuario_id:
                t = Tarea(f["id"], f["usuario_id"], f["nombre"], f["descripcion"], f["materia"], f["fecha_entrega"])
                t.estado = f["estado"]
                t.prioridad = f["prioridad"]
                tareas.append(t)
        return tareas

    def completar_tarea(self, usuario_id, tarea_id):
        with open(self.db_path, "r") as f:
            tareas = json.load(f)
        for t in tareas:
            if t["id"] == tarea_id and t["usuario_id"] == usuario_id:
                t["estado"] = "Completada"
        with open(self.db_path, "w") as f:
            json.dump(tareas, f)

    def eliminar_tarea(self, usuario_id, tarea_id):
        with open(self.db_path, "r") as f:
            tareas = json.load(f)
        tareas = [t for t in tareas if not (t["id"] == tarea_id and t["usuario_id"] == usuario_id)]
        with open(self.db_path, "w") as f:
            json.dump(tareas, f)