class Usuario:
    def __init__(self):
        self.usuario_correcto = "admin"
        self.contrasena_correcta = "1234"

    def validar(self, usuario, contrasena):
        return usuario == self.usuario_correcto and contrasena == self.contrasena_correcta