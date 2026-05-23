from datetime import datetime, date


class Tarea:
    def __init__(self, tarea_id, usuario_id, nombre, descripcion, materia, fecha_entrega):
        self.id = tarea_id
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.materia = materia
        self.fecha_entrega = fecha_entrega
        self.estado = "Pendiente"
        self.prioridad = "Media"

    def calcular_dias_restantes(self):
        from datetime import datetime
        fecha_actual = datetime.now().date()
        fecha_entrega_dt = datetime.strptime(self.fecha_entrega, "%Y-%m-%d").date()
        delta = (fecha_entrega_dt - fecha_actual).days
        return max(delta, 0)