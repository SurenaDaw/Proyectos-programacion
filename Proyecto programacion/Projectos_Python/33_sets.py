#Grupos o conjuntos
#coleccion de datos que no está ordenada que no se pueden repetir y no se pueden acceder a los elementos
numeros = {1, 3, 5, 1, 6, 1, 2, 3 ,7, 1, 2, 4}
print(numeros)
# numeros.add(7)
# numeros.remove(1)
# print(numeros)

numeros2 = [1, 4, 3, 5, 1, 4, 8, 6, 7, 8, 9]
print(numeros2)
numeros2 = set(numeros2)
print(numeros2)

#operador de union, une los dos sets
#numeros3 = (numeros | numeros2)
#operador de interseccion, solo devuelve los valores que estén en ambos sets
#numeros3 = (numeros & numeros2)
#operador de diferencia, muestra los datos del primer conjunto menos los datos del segundo conjunto
#numeros3 = (numeros - numeros2)
#diferencia simetrica, devuelve los elementos que esten en el primero y en el segundo, pero que no esten en los dos a la vez
numeros3 = (numeros ^ numeros2)
print(numeros3)  

if 8 in numeros: 
    print("si esta")
else:
    print("no esta") 