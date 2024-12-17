# v1 = input("Introduce una frase o palabra para saber si es palindromo: ")

# def quitaespacio(texto):

#     palabra = texto.replace(" ","")
#     return palabra.lower()

# def es_palindromo(texto):
#     palabra = ""
#     palindro = ""

#     for char in texto:
#         palabra += char

#     palindro = palabra[::-1]

#     if palindro == palabra:
#         return True
#     else:
#         return False

# palabra = quitaespacio(v1)
# palin = es_palindromo(palabra)

# print(f"La palabra {v1} es {palin}")

entrada = input("Introduce un texto: ").lower()

def no_space(texto):
    sin_espacios = ""
    sin_espacios = texto.replace(" ","")
    return sin_espacios

def invertir(texto):
    inversa = texto[::-1]
    return inversa

def es_palindromo(texto):
    v1 = no_space(texto)
    v2 = invertir(v1)

    return v1 == v2

print(f"La palabra '{entrada}' es palindroma:", es_palindromo(entrada))