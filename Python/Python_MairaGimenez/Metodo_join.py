

#help(str.join)

tupla_str = ("Hola", "Mundo", "Tecnicatura", "Universitaria")
mensaje = " ".join(tupla_str)
print(mensaje)
lista_cursos = ["Java", "Python", "Angular", "Spring"]
mensaje = ", ".join(lista_cursos)
print(mensaje)

cadena = "HolaMundo"
mensaje = ".".join(cadena)
print(mensaje)

diccionario = {"nombre": "Juan", "Apellido": "Perez", "Edad": "18"}
llaves = "-".join(diccionario.keys())
valores = "-".join(diccionario.values())
print(f"Llaves: {llaves}, Type: {llaves}")
print(f"Valores: {valores}, Type: {valores}")