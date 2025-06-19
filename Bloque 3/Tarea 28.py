# Abrimos el archivo en modo lectura ('r')
archivo = open("ejemplo1.txt", "r")

# Leemos línea por línea usando un bucle
for linea in archivo:
    print(linea.strip())  # Mostramos la línea sin saltos de línea adicionales

# Cerramos el archivo
archivo.close()
