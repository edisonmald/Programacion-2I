# Convertir todas las palabras a mayúsculas
with open('mbox.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        print(linea.upper().strip())
        