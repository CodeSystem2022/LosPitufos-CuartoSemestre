from capa_de_datos_persona.Usuario import Usuario
from capa_de_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log

class UsuarioDAO:

    '''
    DAO-> Data ACCESS OBJECT PARA LA TABLA DE USUARIO
    CRUD -> create -read  update -delete
    '''


    -SELECT = 'select * from usuario Order by id usuario'
    -INSERTAR = 'INSERT INTO usuario ( useername , password) VALUES (&s , %s)'
    _ACTUALIZAR =' update USUARIO SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
     with CursorDelPool() as cursor:
         log.debug('Seleccciona usuarios')
         cursor.execute(cls._SELECT)
         registros = cursor.fetchall()
         usuario = []
         for registro in registros:
             usuario = Usuario(registro[0] , registro[1] , registro[2])
             usuario.append(usuario)
             return usuarios

         @classmethod
         def insertar(cls , usuario):
             with CursorDelPool() as cursor:
                 log.debug(f' usuarioa a insertar: { usuario}')
                 valores = (usuario.usename , usuario._password)
                 cursor.execute(cls._INSERT, valores)
                 return cursor.rowcount

                 @classmethod
                 def actualizar(cls, usuario):
                     with CursorDel pool() as cursor:
                     log.debug(f'Usuario actualizado {usuario}')
                     valores = (usuario.username, usuario.password, usuario._id_usuario)
                     cursor.execute(cls._ACTUALIZAR , valores)
                     return cursor.rowcount

                 @classmethod
                 def eliminar(cls.usuario):
                 with CursorDelPool() as cursor:
                 log.debug(f'Usuario eliminado : {usuario}')
                 valores = (usuario._id_usuario,)
                 cursor.execute(cls._ELIMINAR, valores)
                 return cursor.rowcount

