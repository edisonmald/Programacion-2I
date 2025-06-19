# 5. Buscar una palabra específica en un archivo
palabra_buscada = "ecuador"
contador = 0

with open("documento.txt", "r") as archivo:
    for linea in archivo:
        contador += linea.lower().count(palabra_buscada.lower())

print(f"La palabra '{palabra_buscada}' aparece {contador} veces.")