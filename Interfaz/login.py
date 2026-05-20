import tkinter as tk
from tkinter import messagebox

from Model.usuario import Usuario
from interfaz.ventana_principal import VentanaPrincipal


class Login:
    def __init__(self):
        self.usuario = Usuario()

        self.ventana_login = tk.Tk()
        self.ventana_login.title("SIGTA - Inicio de sesión")
        self.ventana_login.geometry("350x250")
        self.ventana_login.resizable(False, False)

        self.crear_interfaz_login()

    def iniciar(self):
        self.ventana_login.mainloop()



