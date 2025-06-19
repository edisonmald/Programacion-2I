# Creamos un archivo de prueba
with open("texto.txt", "w") as f:
    f.write("hola mundo hola universo hola python")

# Leemos el archivo y contamos cuántas veces aparece "hola"
with open("texto.txt", "r") as f:
    contenido = f.read()
    contador = contenido.count("hola")

print("La palabra 'hola' aparece", contador, "veces.")
