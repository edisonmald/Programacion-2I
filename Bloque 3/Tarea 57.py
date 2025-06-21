# Ingresar texto
texto = input("Ingresa una línea de texto: ")

# Separar palabras
palabras = texto.split()

# Contar frecuencias
frecuencia = {}

for palabra in palabras:
    palabra = palabra.lower()
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# Mostrar resultados
print("Frecuencia de palabras:")
for palabra, conteo in frecuencia.items():
    print(palabra, ":", conteo)
