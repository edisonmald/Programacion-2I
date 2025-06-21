# Pedir palabras al usuario
entrada = input("Ingresa varias palabras separadas por espacios: ")

# Convertir a lista
palabras = entrada.split()

# Buscar la palabra más larga
palabra_mas_larga = max(palabras, key=len)

print("La palabra más larga es:", palabra_mas_larga)
