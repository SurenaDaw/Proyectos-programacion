#------ Metodos para trabajar con strings ------
#Las variables de texto tienen sus propios metodos 
variable = "texto de prueba"
print(variable.upper()) #upper() para mayusculas
print(variable.lower()) #lower() minusculas
print(variable.find("e")) #find() busca una cadena, si se repite solo devuele la primera
print(variable.find("rue")) #find() busca una cadena, si se busca un bloque devuelve el inicio
print(variable.replace("Texto", "Letras")) #replace() remplaza un bloque de texto por otro
print(variable.replace("e", "i")) #replace() remplaza un caracte por otro de haber varios se modifican todos

#replace no modifica la variable
print("de" in variable) #con in buscamos una cadena en una variable y devuelve true o false
print("Saprolin " * 4)#de esta forma se multiplica el numero de veces indicado la salida
nombre = "Sergio"
apellido = "Ureña"
nombre_completo = nombre + " " + apellido
usuario = f"{nombre} {apellido}"
print(nombre_completo)
print(usuario)
print(variable.capitalize()) #convierte la primera en mayuscula
print(variable.title())#convierte la primera letra despues de un espacio en mayusucla
v2 = "     letras bonitas escritas     " 
print(v2.strip())#elimina los espacios en blanco a derecha e izquierda

#secuencias de escape
#\n
#\'
#\"
#\\

v3 = '"Palabra entre comillas"'
v4 = '\"Palabra entre comillas\"'
print(v3)
print(v4)