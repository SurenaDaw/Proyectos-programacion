usuarios = [["El bicho", 4], ["Manu", 2], ["Perla", 1], ["Chispa", 3]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)


#transformar o map
#expresion for nombre de cada elemento in lista a iterar
#itera la lista dentro de la sublista y luego toma el primer elemento
nombres= [usuario[0] for usuario in usuarios]
print(nombres)

#filtrar o filter

numero = [id for id in usuarios if id[1] > 2]
print(numero)

#filtrar y tranformar
#devuelve el primer elemento de la sublista pero solo los que cumple la condicion de que el segundo elemento sea < 2
lideres = [usuario[0] for usuario in usuarios if usuario[1] < 2]
print(lideres)