# def hola():
#     print("Hola mundo")

 
# hola()

# def saludo(nombre, apellido):
#     print(f"hola { nombre} {apellido}")


# saludo(input("Introduce tu nombre: "),input("Cual es tu apellido: ")) #Se puede recoger el argumento directamente en la llamada

def saludo(nombre, apellido=""):
    print(f"saludos {nombre} {apellido}")

saludo("sergio")
saludo(apellido="ureña", nombre="Sergio")#Se puede cambiar el argumeto si se indica en la llamada

