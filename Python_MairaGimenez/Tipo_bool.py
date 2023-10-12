#booll contiene valores numeros tru or false
#los tipos numericos d¿es false para el 0 (cero) true para los demas valores
valor = 0
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")

valor = -1
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")

#tipo string -> false "", true demas valores
valor = ''
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")

valor = "HOLA"
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")

#tipo de colecciones -> false pra colecciones vacias
#tipo de colecciones -> true para todas las demas colecciones
#lista
valor = []
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")
valor = [2,3,4]
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")

#tuplas
valor = ()
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")
valor = (5,)
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")

#diccionario
valor = {}
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")
valor = {"Nombre" : "Juan","Apellido" : "Perez"}
resultado = bool(valor)
print(f"valor:  {valor}, resultado  {resultado}")

#sentencias de control con bool
if 0:
    print('Regresa verdadero')
else:
    print('Regresa falso')

#ciclos
variable=0
while variable:
    print("Regresa verdadero")
    break
else:
    print("Regresa falso")