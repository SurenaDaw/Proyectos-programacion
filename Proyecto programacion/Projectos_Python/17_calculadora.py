print("Bienvenido a la calculadora de Sergito")
print("Para salir escribe salir")
print("Las operciones admitidas con sum, mul, div y res")
numero = float(input("Ingresa un número: "))
acciones = ["sum", "res", "mul", "div"]


while True:    
    accion = input("Ingresa una operacion: ").lower()
    if accion == "salir":
        break
    elif accion != "salir" and not (accion in acciones):
        print("Accion invalida")
    if accion == "sum":
        numero  += float(input("Ingresa el siguiente numero: "))
        print(f"El resultado es {numero}")
    elif accion == "res":
        numero  -= float(input("Ingresa el siguiente numero: "))
        print(f"El resultado es {numero}")    
    elif accion == "mul":
        numero  *= float(input("Ingresa el siguiente numero: "))
        print(f"El resultado es {numero}")
    elif accion == "div":
        numero  /= float(input("Ingresa el siguiente numero: "))
        print(f"El resultado es {numero}")