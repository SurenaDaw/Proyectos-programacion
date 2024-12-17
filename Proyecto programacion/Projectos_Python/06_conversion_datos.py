#------ Convertir datos ------
variable = input("Como te llamas corazon de melon:")
#para convertir una variable de tipo es necesario guadarlo en una variable
variable2 = input("Cuantos añitos tienes, princesa:")
variable2 = int(variable2)
variable3 = 45
variable3 = float(variable3)

print(type(variable))
print(type(variable2))
print(type(variable3))
print(variable)
print(variable2)
print(variable3)

#Es necesario convertir todo en un str para poder hacer un print
#print("Te llamas " + variable + " y tienes " + variable2 + " años") esta forma serviria si todas las variables fueran str
print(f"Te llamas {variable} y tienes {variable2} años") #Así formateamos a string todo lo de la cadena pero sin modificar el tipo de dato de las variables
print(type(variable))
print(type(variable2))


#Para el booleano los valores ""(string vacio), 0 ,boolean False y el objeto None. El resto evalua en True
v1 = ""
v2 = ""
v3 = ""
v4 = ""
v5 = ""
v1 = bool("")
v2 = bool(0)
v3 = bool(False)
v4 = bool(None)
v5 = bool("Esto es verdad")