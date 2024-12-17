mascotas = ["Perla", "El bicho", "Chispa", "Tapon", "Olivia", "Jara"]
frutas = ["Manzana", "Fresa", "Manzana", "Cereza", "Platano", "Manzana", "Melon"]

print(f"Hay {frutas.count('Manzana')} manzanas")

print(mascotas.index("Chispa"))

print(mascotas.index("Tapon")) if "Tapon" in mascotas else print("Se ha escapado")
print(mascotas.index("Tapon")) if "Manu" in mascotas else print("Se ha escapado")

