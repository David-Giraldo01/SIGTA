import tkinter as tk
from tkinter import messagebox
from modelo.usuario import Usuario
from interfaz.ventana_principal import VentanaPrincipal


class Login:
    def __init__(self):
        # Conexión con la base de datos
        self.usuarios_db = Usuario()

        # Ventana de login
        self.ventana_login = tk.Tk()
        self.ventana_login.title("SIGTA - Inicio de sesión")
        self.ventana_login.geometry("400x300")
        self.ventana_login.resizable(False, False)

        self.crear_interfaz_login()

    def iniciar(self):
        self.ventana_login.mainloop()

    def crear_interfaz_login(self):
        # Título
        tk.Label(self.ventana_login, text="SIGTA", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(self.ventana_login, text="Sistema de Gestión de Tareas Académicas").pack(pady=5)

        # Campo Usuario
        tk.Label(self.ventana_login, text="Usuario:").pack()
        self.entry_usuario = tk.Entry(self.ventana_login)
        self.entry_usuario.pack(pady=5)

        # Campo Contraseña
        tk.Label(self.ventana_login, text="Contraseña:").pack()
        self.entry_contrasena = tk.Entry(self.ventana_login, show="*")
        self.entry_contrasena.pack(pady=5)

        # Botón Ingresar
        tk.Button(
            self.ventana_login,
            text="Ingresar",
            command=self.validar_login
        ).pack(pady=5)

        # Botón Registrar usuario
        tk.Button(
            self.ventana_login,
            text="Registrar nuevo usuario",
            command=self.registrar_usuario
        ).pack(pady=5)

    def validar_login(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if self.usuarios_db.validar(usuario, contrasena):
            messagebox.showinfo("Éxito", "Inicio de sesión correcto")
            self.ventana_login.destroy()
            ventana_principal = VentanaPrincipal()
            ventana_principal.iniciar()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def registrar_usuario(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        if usuario == "" or contrasena == "":
            messagebox.showwarning("Campos vacíos", "Debe ingresar usuario y contraseña")
            return

        exito = self.usuarios_db.agregar_usuario(usuario, contrasena)
        if exito:
            messagebox.showinfo("Éxito", f"Usuario '{usuario}' registrado correctamente")
        else:
            messagebox.showerror("Error", f"El usuario '{usuario}' ya existe")
