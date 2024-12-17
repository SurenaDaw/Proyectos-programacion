def no_space(texto):#funcion para eliminar espacios en blanco
    nuevo_texto = ""#declara una variable vacia
    for char in texto: #intera la palabra
        if char != " ": #comprueba que el caracte de la palabra sea distitno de un espacio " "
            nuevo_texto += char #si no es espacio en blanco, lo guarda
    return nuevo_texto #devuelve el string sin espacios es blanco

def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)

    return texto.lower() == texto_al_reves.lower()
    
print(es_palindromo("amo la paloma"))
print(es_palindromo("amo las palomitas"))