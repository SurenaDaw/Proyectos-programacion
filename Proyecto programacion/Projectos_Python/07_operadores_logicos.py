#------ Operadores logicos en python ------
edad = 30

#and si todos son true evalua true, si uno es false evalua false
print(edad > 18 and edad < 40)#true
print(edad > 18 and edad > 40)#false
#or si una de las condiciones es true evalua en true, si ninguna es true evalua false
print(edad < 18 or edad < 40)#true
print(edad < 18 or edad > 40)#false
#not invierte el resultado
print(not (edad < 18))#true, porque la edad no es mayor de 18
print(not (edad > 18))#false, porque la edad si es mayor de 18
print(not (edad < 18 or edad > 40))#true
print(not (edad > 18 and edad < 40))#false

