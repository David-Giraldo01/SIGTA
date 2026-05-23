from Model.tarea import Tarea
from Model.priorizador import Priorizador

import json
import os
from Model.tarea import Tarea

# Model/gestor_tareas.py
# Model/gestor_tareas.py
import json
from Model.tarea import Tarea
from Model.priorizador import Priorizador
class GestorTareas:
    def __init__(self, tareas_file="tareas.json"):
        self.tareas_file = tareas_file

        try:
            with open(self.tareas_file, "r") as f:
                json.load(f)
        except:
            with open(self.tareas_file, "w") as f:
                json.dump([], f)

    def crear_tarea(self, usuario_id, nombre, descripcion, materia, fecha_entrega):
        with open(self.tareas_file, "r") as f:
            tareas_data = json.load(f)

        tarea_id = 1
        if tareas_data:
            tarea_id = max(t["id"] for t in tareas_data) + 1

        tarea = Tarea(tarea_id, usuario_id, nombre, descripcion, materia, fecha_entrega)
        tarea.prioridad = Priorizador.asignar_prioridad(tarea)

        tareas_data.append({
            "id": tarea.id,
            "usuario_id": tarea.usuario_id,
            "nombre": tarea.nombre,
            "descripcion": tarea.descripcion,
            "materia": tarea.materia,
            "fecha_entrega": tarea.fecha_entrega,
            "estado": tarea.estado,
            "prioridad": tarea.prioridad
        })

        with open(self.tareas_file, "w") as f:
            json.dump(tareas_data, f, indent=4)

        return tarea

    def listar_tareas(self, usuario_id):
        with open(self.tareas_file, "r") as f:
            tareas_data = json.load(f)

        tareas = []
        for t in tareas_data:
            if t["usuario_id"] == usuario_id:
                tarea = Tarea(t["id"], t["usuario_id"], t["nombre"], t["descripcion"], t["materia"], t["fecha_entrega"])
                tarea.estado = t["estado"]
                tarea.prioridad = t["prioridad"]
                tareas.append(tarea)

        return tareas

    def completar_tarea(self, usuario_id, tarea_id):
        with open(self.tareas_file, "r") as f:
            tareas_data = json.load(f)

        for t in tareas_data:
            if t["id"] == tarea_id and t["usuario_id"] == usuario_id:
                t["estado"] = "Completada"

        with open(self.tareas_file, "w") as f:
            json.dump(tareas_data, f, indent=4)

    def eliminar_tarea(self, usuario_id, tarea_id):
        with open(self.tareas_file, "r") as f:
            tareas_data = json.load(f)

        tareas_data = [t for t in tareas_data if not (t["id"] == tarea_id and t["usuario_id"] == usuario_id)]

        with open(self.tareas_file, "w") as f:
            json.dump(tareas_data, f, indent=4)