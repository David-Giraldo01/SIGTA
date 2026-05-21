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

    def crear_interfaz(self):
        tk.Label(
            self.ventana,
            text="Gestión de Tareas Académicas",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        frame = tk.Frame(self.ventana)
        frame.pack(pady=10)

        tk.Label(frame, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(frame, width=30)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(frame, text="Descripción:").grid(row=1, column=0)
        self.entry_descripcion = tk.Entry(frame, width=30)
        self.entry_descripcion.grid(row=1, column=1)

        tk.Label(frame, text="Materia:").grid(row=2, column=0)
        self.entry_materia = tk.Entry(frame, width=30)
        self.entry_materia.grid(row=2, column=1)

        tk.Label(frame, text="Fecha entrega YYYY-MM-DD:").grid(row=3, column=0)
        self.entry_fecha = tk.Entry(frame, width=30)
        self.entry_fecha.grid(row=3, column=1)

        botones = tk.Frame(self.ventana)
        botones.pack(pady=10)

        tk.Button(botones, text="Agregar tarea", command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(botones, text="Completar tarea", command=self.completar_tarea).grid(row=0, column=1, padx=5)
        tk.Button(botones, text="Eliminar tarea", command=self.eliminar_tarea).grid(row=0, column=2, padx=5)
        tk.Button(botones, text="Ver alertas", command=self.ver_alertas).grid(row=0, column=3, padx=5)

        columnas = ("ID", "Nombre", "Descripción", "Materia", "Fecha", "Estado", "Prioridad")

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=columnas,
            show="headings"
        )

        for columna in columnas:
            self.tabla.heading(columna, text=columna)
            self.tabla.column(columna, width=110)

        self.tabla.pack(pady=20, fill="both", expand=True)

    def agregar_tarea(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        materia = self.entry_materia.get()
        fecha = self.entry_fecha.get()

        if nombre=="" or descripcion =="" or materia =="" or fecha =="":
            messagebox.showwarning("Campos incompletos", "Todos los campos son obligatorios.")
            return

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "La fecha debe tener formato YYYY-MM-DD")
            return

        self.gestor.crear_tarea(nombre, descripcion, materia, fecha)

        messagebox.showinfo("Éxito", "Tarea agregada correctamente")
        self.limpiar_campos()
        self.cargar_tareas()

    def cargar_tareas(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for tarea in self.gestor.listar_tareas():
            self.tabla.insert(
                "",
                tk.END,
                values=(
                    tarea.id,
                    tarea.nombre,
                    tarea.descripcion,
                    tarea.materia,
                    tarea.fecha_entrega,
                    tarea.estado,
                    tarea.prioridad
                )
            )

    def completar_tarea(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Seleccione tarea", "Debe seleccionar una tarea")
            return

        item = self.tabla.item(seleccion)
        id_tarea = item["values"][0]

