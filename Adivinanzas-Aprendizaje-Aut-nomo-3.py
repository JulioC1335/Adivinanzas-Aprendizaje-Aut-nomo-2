import random

def pc_adivina():
    print("¿Qué modo de dificultad quieres? (1, 2 o 3)")
    print("1: 1 al 50")
    print("2: 1 al 100")
    print("3: 1 al 200")

    # Validación de entrada para la dificultad (while True)
    while True:
        try:
            dificultad = int(input("Elige una opción: "))
            if 1 <= dificultad <= 3:
                break
            else:
                print("Opción inválida. Elige 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

    limite_inferior = 1
    limite_superior = 50 * dificultad
    respuesta = ""
    intentos = 0  # Contador de intentos

    print(f"Piensa en un número entre {limite_inferior} y {limite_superior}.")

    while respuesta != "SI":
        intentos += 1
        intento = (limite_inferior + limite_superior) // 2
        respuesta = input(f"¿Estás pensando en el número {intento}? (Si/No): ").upper()

        if respuesta == "SI":
            print(f"¡Adiviné en {intentos} intentos!")
        else:
            # Validación de respuesta "Mayor/Menor" (while True)
            while True:
                respuesta = input(f"¿Tu número es mayor o menor que {intento}? (Mayor/Menor): ").upper()
                if respuesta in ["MAYOR", "MENOR"]:
                    break
                else:
                    print("Respuesta inválida. Escribe 'Mayor' o 'Menor'.")

            if respuesta == "MAYOR":
                limite_inferior = intento + 1
            else:  # (else sin elif)
                limite_superior = intento - 1

def usuario_adivina():
    print("¿Qué modo de dificultad quieres? (1, 2 o 3)")
    print("1: 1 al 50")
    print("2: 1 al 100")
    print("3: 1 al 200")

    # Validación de entrada similar a pc_adivina() (while True)
    while True:
        try:
            dificultad = int(input("Elige una opción: "))
            if 1 <= dificultad <= 3:
                break
            else:
                print("Opción inválida. Elige 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

    numero_secreto = random.randint(1, 50 * dificultad)
    intentos = 0

    # Bucle principal del juego (while True)
    while True:
        intentos += 1
        try:
            intento = int(input("Intenta adivinar el número: "))
            if intento == numero_secreto:
                print(f"¡Adivinaste en {intentos} intentos!")
                break  # Salir del bucle si adivina
            elif intento < numero_secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

# Bucle principal del juego (while True)
while True:
    print("\nBienvenido al Juego de Adivinanzas!")
    print("1. PC Adivina")
    print("2. Usuario Adivina")
    print("3. Finalizar")

    # Validación de entrada para la opción del menú (while True)
    while True:
        try:
            opcion = int(input("Elige una opción: "))
            if 1 <= opcion <= 3:
                break
            else:
                print("Opción inválida. Elige 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

    if opcion == 1:
        pc_adivina()
    elif opcion == 2:
        usuario_adivina()
    elif opcion == 3:
        print("Fin del juego. ¡Gracias por jugar!")
        break