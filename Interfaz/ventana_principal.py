import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

from Model.gestor_tareas import GestorTareas

class VentanaPrincipal:
    def __init__(self):
        self.gestor = GestorTareas()

        self.ventana = tk.Tk()
        self.ventana.title("SIGTA - Gestión de Tareas")
        self.ventana.geometry("850x600")

        self.crear_interfaz()

    def iniciar(self):
        self.ventana.mainloop()

