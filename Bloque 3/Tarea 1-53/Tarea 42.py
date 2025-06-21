texto = input("Escribe algo para guardar en mbox.txt: ")
with open("mbox.txt", "w") as f:
    f.write(texto)
print("Texto guardado en mbox.txt.")