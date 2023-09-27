from logger_base import log
from capa_datos_personas.Usuario import Usuario
from capa_datos_personas.usuarioDao import usuarioDao



opcion = None
while opcion!=5:
    print('Opcion: ')
    print('1. Listar Usuario')
    print('2. Agregar Usuario')
    print('3. Modificar Usuario')
    print('4. Eliminar Usuario')
    print('5. SALIR')
    opcion= int(input('Digite la opcion (1-5): '))
    if opcion==1:
        usuario= Usuario.seleccionar()
        for usuario in usuarioDao:
            log.info(usuario)
    elif opcion==2:
        username_var= input('Digiteel nombre de usuario: ')
        password_var= input('Digite su contraseña: ')
        usuario= Usuario(username= username_var, password=password_var)
        usuario_insertado=usuarioDao.insertar(usuario)
    elif opcion==3:
        id_usuario_var= int(int('Digite el id del usuario que desea modificar: '))
        username_var= input('Digite el nombre del usuario a modificar:')
        password_var=input('Digite la contraseña del usuaeio a modificar:')
        usuario= Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
        usuario_actualizado= usuarioDao.actualizar(usuario)
        log.info(f' Usuario actualizado: {usuario_actualizado}')
    elif opcion==4:
        id_usuario_var=int(input('Digite el id del usuario que desea eliminar: '))
        usuario= Usuario(id_usuario=id_usuario_var)
        usuario_eliminado= usuarioDao.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')
else: 
    log.info('Salimos de la app. HASTA PRONTO!!')