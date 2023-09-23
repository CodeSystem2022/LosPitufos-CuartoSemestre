

# help(str.join)
tupla_srt =('hola' , 'alimnos', 'Tecnicatura' , 'Universitaria')
mensaje = ' '.join(tupla_srt)
print(f'mensaje : {mensaje}')

lista_curso = ['java', 'python', 'Angula', 'sprint']
mensaje = ' , '.join(lista_curso)
print(f'mensaje: { mensaje}')

cadena = 'hola mundo'
mensaje = ' . '.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre': 'juan', 'apellido': 'perez', 'edad': '18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'llaves: {llaves}, type:{type(llaves)}')
print(f'valores : {valores} type : {type(valores)}')