from usuario import *

registro = Registro()
registro.agregar_usuario("Federico", "federico@hotmail.com", "contraseña123")
registro.agregar_usuario("Maria", "maria@example.com", "contraseña456")
print('*'*50)
registro.verificar_usuario("juan@example.com", "contraseña123")
print('*'*50)
registro.eliminar_usuario("maria@example.com")
print('*'*50)
registro.mostrar_usuarios()
print('*'*50)
registro.agregar_usuario("Juan Pérez", "juan@example.com", "contraseña123")