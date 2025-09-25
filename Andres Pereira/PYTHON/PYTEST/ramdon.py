import random

estudiantes = ["Juan", "Ana", "Luis", "Marta", "Carlos"]

numero_aleatorio = random.randint(0, len(estudiantes) - 1)
print(f"El estudiante seleccionado es: {estudiantes[numero_aleatorio]}")