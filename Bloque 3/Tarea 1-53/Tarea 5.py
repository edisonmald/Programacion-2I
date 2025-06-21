def saludo(lang):
    if lang=='es':
        return('hola')
    elif lang=="fr":
        return("Bonjour")
    else:
        return("hello")
print(saludo("es"),"Glenn")
print(saludo("fr"),"Sally")
print(saludo("1"),"Michael")