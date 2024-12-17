mascotas = ["Perla", "El bicho", "Chispa"]

for mascota in enumerate(mascotas):
    print(mascota)
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
# numero=0
# pares=[]
# impares=[]


# while numero <= 100:
#     if numero %2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)
#     numero += 1
# print(pares)
# print(impares)    

inversa = list(reversed(mascotas)) #devuelve los valores a la inversa

print(inversa)

