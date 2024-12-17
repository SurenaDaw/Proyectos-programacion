mascotas = ["Perla", "El bicho", "Chispa", "Tapon", "Olivia", "Jara"]

mascotas.insert(1, "Angel")#añade elemento en el indice indicado
mascotas.append("Carlos")#añade elemento al final

print(f"Mascotas despues de insertar {mascotas}")

mascotas.remove("Angel")#elimina la primera coincidencia
mascotas.pop()#elimina el ultimo pero devuelve el valor
mascotas.pop(3)#elimina el indice seleccionado

del mascotas[1]



print(f"Mascotas despues de eliminar{mascotas}")

mascotas.clear()#vacia la lista

print(f"Mascotas despues del clear{mascotas}")