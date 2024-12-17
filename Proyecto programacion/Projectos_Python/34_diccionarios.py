#son sonuna coleccion de datos agrupados por una llave y un valor
#se define con llaves{string: valor}, se separan por ,
punto = {"x":25, "y": 45}
print(punto)
#se accede a traves del string no de la posicion y devuelve el valor asociado a la llave
print(punto["x"])
#se crea una nueva llave
punto["z"] = -159
print(punto)

if "lala" in punto:
    print("si esta")
else: print("no esta")
#con el metodo get le pasamos una llave y devuelve el valor
print(punto.get("z"))
print(punto.get("k"))#en caso de no existir la llave, devueleve none
print(punto.get("lala", 98))#se añade un valor por defecto en caso de que la llave no exista
#eliminar valores
del punto["y"]
del (punto["z"])
print(punto)

punto["y"]= 5

for i in punto:
    print(i)

for j in punto:
    print(j, punto[j])

#devuelve tuplas por cada valor
for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"dni":1, "nombre": "Miki"},
    {"dni":2, "nombre": "Ray"},
    {"dni":3, "nombre": "Vision"},
    {"dni":4, "nombre": "Manu"},
    {"dni":5, "nombre": "Sergito"}
]

for usuario in usuarios:
    print(usuario["nombre"])
