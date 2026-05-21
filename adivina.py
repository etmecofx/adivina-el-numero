import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Bienvenido al juego Adivina el Número")
    print("Estoy pensando en un número entre 1 y 100...")

    while True:
        try:
            intento = int(input("Tu intento: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("Muy bajo, intenta de nuevo.")
        elif intento > numero_secreto:
            print("Muy alto, intenta de nuevo.")
        else:
            print(f"¡Correcto! Adivinaste el número {numero_secreto} en {intentos} intento{'s' if intentos != 1 else ''}.")
            break

jugar()
