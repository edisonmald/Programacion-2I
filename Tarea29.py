#Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))
print("La suma total es:", suma)

#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
numero_secreto = 5
intento = int(input("Adivina el número entre 1 y 100: "))
while intento != numero_secreto:
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
    intento = int(input("Intenta de nuevo: "))
print("¡Felicidades! Adivinaste el número.")

#Validar contraseña (repetir hasta que coincida con una guardada).
contraseña = "patito123"
entrada = input("Ingresa la contraseña: ")
while entrada != contraseña:
    print("Contraseña incorrecta. Intenta de nuevo.")
    entrada = input("Ingresa la contraseña: ")
print("¡Contraseña correcta! Acceso concedido.")

#Simular un cajero automático (menú: retirar, depositar, salir).
opcion = ""
while opcion != "3":
    print(" Bienvenido a Nuestro cajero ")
    print(" Ingrese 1 para retirar dinero")
    print(" Ingrese 2 para depositar dinero")
    print(" Ingrese 3 para salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        monto = float(input("¿Cuánto deseas retirar? "))
        print("Has retirado $",monto )
    elif opcion == "2":
        monto = float(input("¿Cuánto deseas depositar? "))
        print("Has depositado $",monto)
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Hasta luego!")
    else:
        print("Opción no válida. Intenta de nuevo.")

#Calcular la raíz cuadrada por aproximación (método babilónico).
numero = 20
tolerancia = 0.0001
tolerancia_cuadrada = tolerancia * tolerancia
estimacion = numero / 2.0
nueva_estimacion = 0.5 * (estimacion + numero / estimacion)
while (nueva_estimacion - estimacion) * (nueva_estimacion - estimacion) >= tolerancia_cuadrada:
    estimacion = nueva_estimacion
    nueva_estimacion = 0.5 * (estimacion + numero / estimacion)
print("La raíz cuadrada aproximada de", numero, "es", nueva_estimacion)

#Contar dígitos de un número entero (ej: 456 → 3).
numero = 456
original = numero  
cantidad_digitos = 0
while numero > 0:
    numero //= 10
    cantidad_digitos += 1
print(f"El número {original} tiene {cantidad_digitos} dígitos.")

#Generar la secuencia de Fibonacci hasta un límite.
limite = int(input("Ingresa el limite: "))
a, b = 0, 1
secuencia = [a]
while a <= limite:
    a, b = b, a + b
    if a <= limite:
        secuencia += [a]  
print(f"Secuencia de Fibonacci hasta {limite}:")
print(secuencia)

#Encontrar números primos en un rango dado.
inicio = 10
fin = 50
n = inicio
while n <= fin:
    if n > 1:
        i = 2
        es_primo = True
        while i * i <= n:
            if n % i == 0:
                es_primo = False
                break
            i += 1
        if es_primo:
            print(n)
    n += 1

#Simular un temporizador (contar regresivamente desde N).
N = int(input("Ingrese un numero: "))
while N > 0:
    print(f"Tiempo restante: {N} segundos")
    N -= 1
print("¡Tiempo terminado!")

#Leer archivos línea por línea hasta fin de archivo.
f = open("archivo.txt", "r")
linea = f.readline()
while linea != "":
    print(linea, end="")
    linea = f.readline()
f.close()
print("fin del programa")
