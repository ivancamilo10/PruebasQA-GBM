import random

def tirar_dado():

    dado1= random.randint(1, 6)
    dado2= random.randint(1, 6)

    return dado1, dado2

def juego():
    print("¡Bienvenido al juego de los dados!")

    while True:
        opcion = input("¿Quieres tirar los dados? (s/n): ").lower()
        if opcion == "s":
            d1,d2 = tirar_dado()
            print(f"Has tirado un {d1} y {d2}. (total: {d1 + d2})")
        elif opcion == "n":
            print("¡Gracias por jugar! ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa 's' para sí o 'n' para no.")

juego()