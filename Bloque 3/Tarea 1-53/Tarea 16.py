while True:
    line=input("Ingrese un caracter: ")
    if line[0]=="*":
        continue
    if line=="terminado":
        break
    print(line)
print("terminado")

for i in [5,4,3,2,1]:
    print(i)
print("Blastoff")