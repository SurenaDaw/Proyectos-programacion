#------ Ejercicio de conversion de temperatura ------

temperatura = float(input("Que temperatura hace:"))

escala = input("Farenheith (F) o Celsius (C)").lower()

if escala == "c":
    temperatura = (temperatura * 9/5) + 32 #convierte la temperatura de celsius a faren
    print(f"La temperatura es {temperatura} grados F")
elif escala == "f":
    temperatura = (temperatura - 32) * 5/9 #convierte la tempetaruta de faren a celsius
    print(f"La temperatura es {temperatura} grados C")
else:
    print("Escala incorrecta")

