import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

from Model.gestor_tareas import GestorTareas

class VentanaPrincipal:
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
        self.gestor = GestorTareas()
        self.ventana = tk.Tk()
        self.ventana.title("SIGTA - Gestión de Tareas")
        self.ventana.geometry("850x600")
        self.crear_interfaz()
        self.cargar_tareas()

    def iniciar(self):
        self.ventana.mainloop()

    def crear_interfaz(self):
        tk.Label(self.ventana, text="Gestión de Tareas Académicas", font=("Arial", 18, "bold")).pack(pady=10)
        frame = tk.Frame(self.ventana)
        frame.pack(pady=10)
        tk.Label(frame, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(frame, width=30)
        self.entry_nombre.grid(row=0, column=1)
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
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for c in columnas:
            self.tabla.heading(c, text=c)
            self.tabla.column(c, width=110)
        self.tabla.pack(pady=20, fill="both", expand=True)

    def cargar_tareas(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        tareas = self.gestor.listar_tareas(self.usuario_id)
        for t in tareas:
            self.tabla.insert("", tk.END, values=(t.id, t.nombre, t.descripcion, t.materia, t.fecha_entrega, t.estado, t.prioridad))

    def agregar_tarea(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        materia = self.entry_materia.get()
        fecha = self.entry_fecha.get()
        if nombre == "" or descripcion == "" or materia == "" or fecha == "":
            messagebox.showwarning("Campos incompletos", "Todos los campos son obligatorios")
            return
        tarea = self.gestor.crear_tarea(self.usuario_id, nombre, descripcion, materia, fecha)
        self.cargar_tareas()
        messagebox.showinfo("Éxito", f"Tarea '{tarea.nombre}' agregada")

    def completar_tarea(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Seleccione tarea", "Debe seleccionar una tarea")
            return
        item = self.tabla.item(seleccion)
        tarea_id = item["values"][0]
        self.gestor.completar_tarea(self.usuario_id, tarea_id)
        self.cargar_tareas()

    def eliminar_tarea(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Seleccione tarea", "Debe seleccionar una tarea")
            return
        item = self.tabla.item(seleccion)
        tarea_id = item["values"][0]
        self.gestor.eliminar_tarea(self.usuario_id, tarea_id)
        self.cargar_tareas()

    def ver_alertas(self):
        tareas = self.gestor.listar_tareas(self.usuario_id)
        mensajes = []
        from datetime import datetime, date
        for t in tareas:
            fecha_entrega = datetime.strptime(t.fecha_entrega, "%Y-%m-%d").date()
            dias = (fecha_entrega - date.today()).days
            if t.estado != "Completada":
                if dias < 0:
                    mensajes.append(f"La tarea '{t.nombre}' está vencida")
                elif dias == 0:
                    mensajes.append(f"La tarea '{t.nombre}' vence hoy")
                elif dias <= 2:
                    mensajes.append(f"La tarea '{t.nombre}' vence en {dias} día(s)")
        if mensajes:
            messagebox.showwarning("Alertas", "\n".join(mensajes))
        else:
            messagebox.showinfo("Alertas", "No hay tareas próximas a vencer")

