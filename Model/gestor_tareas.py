from Model.tarea import Tarea
from Model.priorizador import Priorizador

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1

    def crear_tarea(self, nombre, descripcion, materia, fecha_entrega):
        tarea = Tarea(
            self.contador_id,
            nombre,
            descripcion,
            materia,
            fecha_entrega
        )

        tarea.prioridad = Priorizador.asignar_prioridad(tarea)