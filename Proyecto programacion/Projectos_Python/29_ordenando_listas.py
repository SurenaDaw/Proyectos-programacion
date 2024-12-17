numeros = [10, 2, 5, 7, 6, 1, 3, 4, 8 ]

# print(numeros)

# numeros.sort() #ordena los valores numericos de menor a mayor
# print(numeros)

# numeros.sort(reverse=True) #ordena los valores numericos de mayor a menos
# print(numeros)

# numeros2 = sorted(numeros, reverse=True)#devuelve una nueva lista ordenando los valores numericos
# print(numeros2)

usuarios1 = [[4, "El bicho"], [2, "Manu"], [1, "Perla"], [3, "Chispa"]]
usuarios2 = [["El bicho", 4], ["Manu", 2], ["Perla", 1], ["Chispa", 3]]
# usuarios2.sort()
# print(usuarios2)


#funcion que devuelve el indice del elemento
#al usar .sort(key) se pasa automaticamente cada elemento de la lista como argumento
def ordena(elemento):
    return elemento[1]

usuarios3 = usuarios2.pop(1)

usuarios2.sort(key=ordena)
print(usuarios3)