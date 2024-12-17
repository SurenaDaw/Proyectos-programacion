usuarios = [["El bicho", 4], ["Manu", 2], ["Perla", 1], ["Chispa", 3]]

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

numeros = list(filter(lambda usuario: usuario[1] >1, usuarios ))
print(numeros)