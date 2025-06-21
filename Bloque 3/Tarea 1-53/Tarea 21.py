# Ejercicio 1: Conteo Regresivo con while.
contador = 10

while contador > 0:
    print(contador)
    contador -= 1

print("¡Despegue!")

# Ejercicio 2: Adivina la Palabra Secreta (while y break).
palabra_secreta = "Universidad"

while True:
    intento = input("Adivina la palabra secreta: ")
    
    if intento == palabra_secreta:
        print("¡Has adivinado la palabra!")

    else:
        print("Inténtalo de nuevo.")

# Ejercicio 3: Procesador de Entradas con continue.
while True:
    entrada = input("Ingresa texto: ")

    if entrada == "#":
        continue
    elif entrada == "listo":
        print("¡Procesamiento terminado!")

    else:
        print(entrada.upper())

# Ejercicio 4: Lista de Invitados con for.

invitados = ['Mateo', 'Andy', 'Justin', 'Edison']
for nombre in invitados:
    print(f"Hola {nombre}, ¡bienvenida a la fiesta!")

# Ejercicio 5: Encontrando el Número Mayor (for)
numeros = [3, 41, 12, 9, 74, 15, 1, 55]
mayor_hasta_ahora = -1
for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero
print("El número más grande es:", mayor_hasta_ahora)

#Ejercicio 6: Conteo de Elementos Pares (for y condicional)
numeros = [2, 5, 8, 11, 14, 17, 20, 23]
contador = 0
for numero in numeros:
    if numero % 2 == 0:
        contador += 1
print("Cantidad de números pares:", contador)

# Ejercicio 7: Suma de Todos los Números (for)
numeros = [10, 20, 30, 40, 50]
suma_total = 0
for numero in numeros:
    suma_total += numero
print("La suma total es:", suma_total)

# Ejercicio 8: Cálculo del Promedio (for)
numeros = [10, 15, 20, 25, 30]
suma_total = 0
conteo = 0
for numero in numeros:
    suma_total += numero
    conteo += 1
if conteo > 0:
    promedio = suma_total / conteo
    print("El promedio es:", promedio)
else:
    print("La lista está vacía, no se puede calcular el promedio.")

# Ejercicio 9: Filtrando Números Mayores que un Valor (for)
numeros = [5, 25, 12, 33, 18, 45, 7]
umbral = int(input("Ingresa un número umbral: "))
print("Números mayores que el umbral:")
for numero in numeros:
    if numero > umbral:
        print(numero)

# Ejercicio 10: Búsqueda de un Valor Específico (for y booleano)
numeros = [9, 41, 12, 3, 74, 15]
encontrado = False
for numero in numeros:
    if numero == 3:
        encontrado = True
        break
print("El valor 3 fue encontrado:", encontrado)

# Ejercicio 11: Encontrando el Número Menor (for y None)
numeros = [30, 10, 5, 25, 50, 2]
menor_hasta_ahora = None
for numero in numeros:
    if menor_hasta_ahora is None:
        menor_hasta_ahora = numero  
    elif numero < menor_hasta_ahora:
        menor_hasta_ahora = numero 
print("El número menor es:", menor_hasta_ahora)