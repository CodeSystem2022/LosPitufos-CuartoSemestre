
#help(str.split)

curso = 'java javascrip Node Python Diseño'
lista_cursos = curso.strip()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

curso_separado_coma = 'java,python,node,javascrip,sring'
lista_cursos = curso_separado_coma.split(',' , 2)
print(f'lista de cursos: {lista_cursos}')
print(len(lista_cursos))