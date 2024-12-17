
saludo = "Estoy fuera de la funcion"
miki = "Estoy dentro de la funcion"
manu = 23

def saludar():
    saludo = "Hola mundo"
    return saludo

def holamiki():
    global miki
    print(miki)

def holamanu():
    global manu
    manu = "Hola holita"
    return manu

c = saludar()


print(c)
print(saludo)
holamiki()
print(manu)
print(holamanu())