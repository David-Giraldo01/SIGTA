from datetime import date

class Tarea:

    def __init__(self, id, nombre, materia):

        self.id = id
        self.nombre = nombre
        self.materia = materia
        self.estado = "Pendiente"

    def completar(self):
        self.estado = "Completada"

    def calcular_dias_restantes(self):
        return 2

tarea1 = Tarea(1,"Parcial POO","Programación")


print("Nombre:", tarea1.nombre)
print("Materia:", tarea1.materia)
print("Estado:", tarea1.estado)

class Priorizador:


    @staticmethod

    def asignar_prioridad(tarea):
        dias = tarea.calcular_dias_restantes()
        if dias <=2:
            return "Alta"
        elif dias <=7:
            return "Media"
        else:
            return "Baja"

prioridad = Priorizador.asignar_prioridad(tarea1)
print("Prioridad:", prioridad)



class Gestor:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def listar_tareas(self):
        print("\n===== LISTADO DE TAREAS =====")
        for tarea in self.tareas:
            print(
                "ID:", tarea.id,
                "| Nombre:", tarea.nombre,
                "| Materia: ", tarea.materia,
                "| Estado: ", tarea.estado
            )

gestor = Gestor()
gestor.agregar_tarea(tarea1)
gestor.listar_tareas()