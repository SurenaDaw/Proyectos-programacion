#Es una funcion anonima simple que no necesita de la palabra reservada def, se suelen usar para realizar funciones de un solo uso

usuarios = [["El bicho", 4], ["Manu", 2], ["Perla", 1], ["Chispa", 3]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key= lambda el: el[1])
print(usuarios)
