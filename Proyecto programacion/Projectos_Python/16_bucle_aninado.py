for j in range(3):
    for k in range(2):
        print(f"los numeros {j} y {k}")

# --- triangulo
filas = int(input("Introduce un numero: "))
for i in range(1, filas + 1):
    espacios = " " * (filas - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

#--- triangulo inverso
# filas = int(input("Introduce un numero: "))
# for i in range(filas, 0, -1):
#     espacios = " " * (filas - i)
#     asteriscos = "*" * (2 * i - 1)  
#     print(espacios + asteriscos)