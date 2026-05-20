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

        self.tareas.append(tarea)
        self.contador_id +=1

    def listar_tareas(self):
        return self.tareas

    def completar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False

    def eliminar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False

    def obtener_alertas(self):
        alertas: []

        for tarea in self.tareas:
            dias = tarea.calcular_dias_restantes()

            if tarea.estado != "Completada":
                if dias <0:
                    alertas.append(f"La tarea '{tarea.nombre}' está vencida.")
                elif dias == 0:
                    alertas.append(f"La tarea '{tarea.nombre}' vence hoy.")
                elif dias <= 2:
                    alertas.append(f"La tarea '{tarea.nombre}' vence en {dias} día(s).")

        return alertas