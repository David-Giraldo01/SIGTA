# Model/priorizador.py
class Priorizador:
    @staticmethod
    def asignar_prioridad(tarea):
        dias = tarea.calcular_dias_restantes()
        if dias <= 2:
            return "Alta"
        elif dias <= 7:
            return "Media"
        else:
            return "Baja"