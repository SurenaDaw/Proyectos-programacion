colores = ["Verde", "Rojo", "Azul", "Blanco", "Negro"]
colores.insert(3 , "Gruul") #con insert añade un elemento en el indice que le indiquemos
colores.insert(0, "Rakdos") #indice 0 para añadir al inicio
colores.insert(-1, "Azorio") #indice -1 para añadir al final
colores.remove("Blanco") #con remove eliminamos el elemento
print("Rakdos" in colores) #devuelve true si el elemento esta en la lista y false si no
#colores.clear() #elimina el listado
print(len(colores))
print(colores)

colores2 = ["Verde", "Rojo", "Azul", "Blanco", "Negro"]
colores2.insert(6, "Orzhov")
print(colores2[6]) #si te pasas del indice se añade en el último hueco disponible 