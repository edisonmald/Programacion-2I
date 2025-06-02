#1.	Crear una función multiplicar(x, y) que retorne el producto de dos números.
x=float(input("Ingrese un número: "))
y=float(input("Ingrese otro número: "))
def multiplicar(x, y):
    return x * y
resultado = multiplicar(x, y)
print("El resultado es:", resultado)

#2.	Crear una función es_par(numero) que retorne True si el número es par.
def es_par(numero):
    return numero % 2 == 0
numero = int(input("Ingrese un número: "))
if es_par(numero):
    print("El número es par")
else:
    print("El número es impar")

#3.	Crear una función presentarse(nombre, edad) que imprima un mensaje con tus datos.
def presentarse(nombre, edad):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")
presentarse("Edison", 18)
