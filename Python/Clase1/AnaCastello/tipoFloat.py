#Profunduzando en el tipo float
a=3.0

#Constrictor de tipo float -> pueden recibit int y str
a=float(10)
a=float('10')
print(f'a: {a:.2f}')

#Notacion exponencial (valores + o -)
a= 3e5
print(f'a: {a:.2f}')

a= 3e-5
print(f'a: {a:.5f}')

#Cualquier calculo que incluye un float, todo cambia a float
a= 4.0+ 5
print(f'a: {a}')
print(type(a))