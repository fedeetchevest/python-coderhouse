class Registro:   
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, nombre, correo, contraseña):
        if correo in self.usuarios:
            print("El correo electrónico ya está registrado.")
        else:
            self.usuarios[correo] = {"nombre": nombre, "contraseña": contraseña}
            print("Usuario registrado correctamente.")

    def verificar_usuario(self, correo, contraseña):
        if correo in self.usuarios:
            if self.usuarios[correo]["contraseña"] == contraseña:
                print("Inicio de sesión exitoso.")
            else:
                print("Contraseña incorrecta.")
        else:
            print("Correo electrónico no registrado.")

    def eliminar_usuario(self, correo):
        if correo in self.usuarios:
            del self.usuarios[correo]
            print("Usuario eliminado correctamente.")
        else:
            print("Correo electrónico no registrado.")

    def mostrar_usuarios(self):
        if self.usuarios:
            print("Usuarios registrados:")
            for correo, datos in self.usuarios.items():
                print(f"Correo: {correo}, Nombre: {datos['nombre']}")
        else:
            print("No hay usuarios registrados.")