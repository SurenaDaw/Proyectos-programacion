#------ Como funcionan los operadores de comparacion ------
n1 = 4 
n2 = 9
print(n1 < 4)
print(n1 <= 4)
print(n1 > 4)
print(n1 >= 4)
print(n1 == 4)
print(n1 == n2)
print(n1 != n2)

# Los operadores de comparacion se pueden encadenar

edad = 14

if 15 <= edad <= 65:
    print("Puedes pasar")
else:
    print("No te bañas")