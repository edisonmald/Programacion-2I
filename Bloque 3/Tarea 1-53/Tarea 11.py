def convertir_temperatura():
    valor = float(input("Ingresar la temperatura: "))
    unidad = input("Ingrese 'C' para convertir a Celsius o 'F' para convertir a Fahrenheit: ")

    if unidad == "F":
        resultado = (valor * 9/5) + 32  # Celsius a Fahrenheit
        print(valor,"°C equivale a", round(resultado,2), "°F")
    elif unidad == "C":
        resultado = (valor - 32) * 5/9  # Fahrenheit a Celsius
        print(valor, "°F equivale a", round(resultado,2), "°C")
    else:
        print("Unidad no válida. Ingrese 'C' o 'F'.")
convertir_temperatura()
