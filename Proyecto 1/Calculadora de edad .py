nombre=input("Ingresa tu nombre: ")
fdn=int(input("Ingresa tu año de nacimiento: "))
edad= 2025-fdn
print("Hola ", nombre, " tienes ", edad," años de edad."  )
if edad>18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")