palabra=input("Ingresa una palabra en minusculas: ")
a= 0
e= 0
i= 0
o= 0
u= 0
for letra in palabra:
    if letra=="a" :
        a+=1
    elif letra=="e" :
        e+=1
    elif letra=="i":
        i+=1
    elif letra=="o":
        o+=1
    elif letra=="u":
        u+=1
print("El número de vocales es:", a+e+i+o+u)
print("Las veces que aprecio a son: ",a )
print("Las veces que aprecio e son: ",e )
print("Las veces que aprecio i son: ",i )
print("Las veces que aprecio o son: ",o )
print("Las veces que aprecio u son: ",u )