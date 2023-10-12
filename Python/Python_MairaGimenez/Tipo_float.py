#Profundizamos en tipo float
a = 3.0
print(f"a: {a:.4f}")

#Construccion de tipo float => puede recibir enteros y tipo string
a = float(10) #le pasamos un tipo float
print(f"a: {a:.4f}")
a = float("10")
print(f"a: {a:.4f}")

#Notacion exponencial(valores positivos o negativos)
a = 3e5
print(f"a:  {a}")

a = 3e-5
print(f"a:  {a}")

#Cualquier calculo que incluye un float, todo cambia a float

a = 4.0 + 5
print(a)
print(type(a))