from datetime import datetime, date


class Tarea:
    def __init__(self, id_tarea, nombre, descripcion, materia, fecha_entrega):
        self.id = id_tarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha_entrega = fecha_entrega
        self.estado = "Pendiente"
        self.prioridad = "Sin asignar"

    def completar(self):
        self.estado = "Completada"

    def calcular_dias_restantes(self):
        fecha = datetime.strptime(self.fecha_entrega, "%Y-%m-%d").date()
        return (fecha - date.today()).days