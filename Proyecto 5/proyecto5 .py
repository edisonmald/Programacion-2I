#calculadora de promedio de calificaciones.
#1.pide al usuario que escriba su nombre.
#2.solicita 4 calificaciones (numeros enteros entr0 y 20).
#3.calcula el promedio de las 4 calificaciones.
#4.muestra un mensaje como juan, tu promnedio es 16.felicitaciones aprobaste
#5.si el promedio es menor a 14 muestra "los siento juan, estas reprobrado"
nombre=input("Por favor ingrese su nombre: ")
calificacion1=int(input("ingrese su primera calificacion: "))
calificacion2=int(input("ingrese su segunda calificacion: "))
calificacion3=int(input("ingrese su tercera calificacion: "))
calificacion4=int(input("ingrese su cuarta calificacion: "))
promedio=(calificacion1+calificacion2+calificacion3+calificacion4)/4
print(nombre,"tu promedio es: ",promedio)
if promedio>=14:
    print("felicitaciones aprobaste")
else:
    print("los siento",nombre,"estas reprobrado")
print("ese es su promedio")