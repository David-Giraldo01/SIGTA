from datetime import date

class Tarea:

    def __init__(self, id, nombre, materia):

        self.id = id
        self.nombre = nombre
        self.materia = materia
        self.estado = "Pendiente"


    def completar(self):

        self.estado = "Completada"

tarea1 = Tarea(1,"Parcial POO","Programación")


print("Nombre:", tarea1.nombre)
print("Materia:", tarea1.materia)
print("Estado:", tarea1.estado)