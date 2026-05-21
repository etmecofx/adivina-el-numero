import random

NIVELES = {
    "1": ("Fácil",   1,  50, 10),
    "2": ("Medio",   1, 100,  7),
    "3": ("Difícil", 1, 200,  5),
}

def elegir_nivel():
    print("\nElige el nivel de dificultad:")
    print("  1. Fácil   (1-50,  10 intentos)")
    print("  2. Medio   (1-100,  7 intentos)")
    print("  3. Difícil (1-200,  5 intentos)")
    while True:
        opcion = input("Tu elección (1/2/3): ").strip()
        if opcion in NIVELES:
            return NIVELES[opcion]
        print("Opción inválida, elige 1, 2 o 3.")

def jugar():
    nombre, minimo, maximo, limite = elegir_nivel()
    numero_secreto = random.randint(minimo, maximo)
    intentos = 0

    print(f"\n--- Nivel {nombre} ---")
    print(f"Estoy pensando en un número entre {minimo} y {maximo}.")
    print(f"Tienes {limite} intentos.\n")

    while intentos < limite:
        restantes = limite - intentos
        try:
            intento = int(input(f"Tu intento ({restantes} restante{'s' if restantes != 1 else ''}): "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        intentos += 1

        if intento < minimo or intento > maximo:
            print(f"Ingresa un número entre {minimo} y {maximo}.")
            intentos -= 1
            continue

        if intento < numero_secreto:
            print("Muy bajo, intenta de nuevo.")
        elif intento > numero_secreto:
            print("Muy alto, intenta de nuevo.")
        else:
            print(f"\n¡Correcto! Adivinaste el {numero_secreto} en {intentos} intento{'s' if intentos != 1 else ''}.")
            return

    print(f"\nSin intentos. El número era {numero_secreto}.")

def main():
    print("=== Adivina el Número ===")
    while True:
        jugar()
        respuesta = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if respuesta != "s":
            print("¡Hasta luego!")
            break

main()
