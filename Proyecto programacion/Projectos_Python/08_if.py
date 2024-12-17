#------ Uso del if en Python ------

nota = 99


#es necesario indentar bien si no no funciona


if nota >= 100:
    print("enhorabuena")
    
#si la primera condición no es true, no ejecutaria nada sin clausula else

if nota >= 100:
    print("enhorabuena")
else:
   print("aprobado")


#evalua de arriba a abajo

if nota < 50:
    print("suspenso")
elif nota > 50:
   print("aprobado")
elif nota > 90:
    print("super aprobado")

#al ser nota > de 50 el segun if ya no lo esta evaluando
    
if nota < 50:
    print("suspenso")
elif nota > 90:
   print("super aprobado")
elif nota > 50:
    print("aprobado")
    
