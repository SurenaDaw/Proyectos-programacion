#------ Creacion y uso de listas en Python ------
colores = ["Verde", "Rojo", "Azul", "Blanco", "Negro"]
print(colores)
print(colores[2])
colores[2] = "Gruul"
print(colores)
print(colores[-3])#indice negativo indica que empieza por el final -1 es el ultimo elemento, -2 el penultimo, etc
print(colores[1:3])#con : indicamos un rango que queremos seleccionar pero no incluye el ultimo elemento
print(colores[:3])# si no indicamos nada en el primer valor, empezara con el primero hasta llegar al que le hemos indicado, sin mostrar ese
print(colores[2:])# si no indicamos nada en ultimo valor, empezara a contar desde el valor que hemos puesto hasta el final
print(colores[::-1])#sirve para invertir la lista
inv_colores= (colores[::-1])
print(inv_colores) 

numeros = [0] * 5#añade la cantidad de veces indicada el contenido de la lista
numeros2 = [1, 3, 5] * 5#añade la cantidad de veces indicada el contenido de la lista
print(numeros)
print(numeros2)

mezcla = numeros + numeros2 #se esta forma se concatenan dos listas
print(mezcla)

rango = list(range(0 , 16))
print(rango)

rangostg = list("Hola mundo")
print(rangostg[::2])#toma un elemento si y otro no empezando por el primero (0)
print(rangostg[1::2])#toma un elemento si y otro no empezando por el indicado (1)
print(rangostg[1:6:2])#toma un elemento si y otro no empezando por el indicado (1) hasta el indicado(6)
print(rangostg[4::-1])#desde el indicado hasta el final, de forma inversa

v1, v2, v3, v4, v5 = colores #De esta forma asignamos a cada varible un valor de la lista, pero hay que usar tantas variables como elementos haya
v6, *otros = colores #se guarda el primer valor en la variable v6 y el resto en otros
v7, v8, *v9, v10, v11 = colores #de esta forma se guardan el primero y el segundo, el resto, y el penultimo y ultimo
print(f"Los colores en magic son {v1}, {v2}, {v3}, {v4}, {v5}")
print(v6)
print(otros)