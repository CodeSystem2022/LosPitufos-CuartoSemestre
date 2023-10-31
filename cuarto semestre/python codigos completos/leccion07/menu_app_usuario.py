from capa_datos_persona.usuario_dao import usuarioDAO
from loger_base import log


opcion= None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('3.Modificar Usuario')
    print('4. Eliminar usuario')
    print('5. salir')
    opcion = int(input('dijite la opcion (1-5 :'))
    if opcion ==1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

elif opcion == 2:
              username_var = input('dijite el nombre de usuario:')
              password_var = input('dijite su contraseña')
              usuario = Usuario(username=username_var, password=password_var)
              usuario_insertado = UsuarioDAO.insertar(usuario)
              log.info(f'usuario insertado: {usuario_insertado}')
    else:
        log.info('salimos de la aplicacion .hasta luego ')
