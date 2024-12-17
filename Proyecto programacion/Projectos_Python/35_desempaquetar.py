lista = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista)

lista2 = [5, 6, 7, 8]

lista3 =["Hola", *lista, "Mundo", *lista2]
print(lista3)

punto1= {"x": 45, "y": "hola"}
punto2= {"y": 26}
punto3= {"Z": 19}


#al asignar propiedades si hay duplicados prevalece la que esta mas a la derecha
nuevoPunto = {**punto1, **punto2, **punto3}
print(nuevoPunto)