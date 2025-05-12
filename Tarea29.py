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

#Contar dígitos de un número entero (ej: 456 → 3).

#Generar la secuencia de Fibonacci hasta un límite.

#Encontrar números primos en un rango dado.

#Simular un temporizador (contar regresivamente desde N).

#Leer archivos línea por línea hasta fin de archivo.