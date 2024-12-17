def suma(a , b):
    print(a + b)

suma(5 , 5)

def operacion(*numeros):
    digito = 0
    for numero in numeros:
        digito += numero
    print(digito)

operacion(5, 6)
operacion(7, 23, 56)
operacion(-4, 25, -232, 452)

