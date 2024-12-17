#es lo mismo que una lista pero no se puede modificar, agregar o eliminar elementos
#se define como una lista pero con parentesis
numeros = (1, 3, 5, 7)
nombres = ["Manu", "Perla", "El bicho", "Chispa"]

print(numeros)

#una lista convertida a tupla con la funcion tuple
print(nombres)
numes = tuple(nombres)
print(numes)

#creamos lista en base a la tupla y la modificamos
listaNumeros = list(numeros)
listaNumeros[0] = 55
print(listaNumeros)



