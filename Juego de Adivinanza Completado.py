import random

def obtener_dificultad():
    """Obtiene y valida la elección de dificultad del jugador."""
    while True:
        try:
            print("\n¿Qué modo de dificultad quieres? (1, 2 o 3)")
            print("1: 1 al 50  |  Vidas: 5")
            print("2: 1 al 100 |  Vidas: 7")
            print("3: 1 al 200 |  Vidas: 10")
            dificultad = int(input("Elige una opción: "))
            if 1 <= dificultad <= 3:
                return 50 * dificultad, [5, 7, 10][dificultad - 1]  # Retorna límite superior y vidas
            else:
                print("Opción inválida. Elige 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

def adivinar_numero(limite_superior, vidas, es_pc=False):
    """Lógica principal para adivinar el número (PC o usuario)."""
    numero_secreto = random.randint(1, limite_superior) if not es_pc else None
    intentos = 0
    limite_inferior = 1

    while vidas > 0:
        print(f"\nTe quedan {vidas} vidas.") if not es_pc else None
        intentos += 1

        if es_pc:
            intento = max(limite_inferior, (limite_inferior + limite_superior) // 2)
            print(f"¿Estás pensando en el número {intento}?")
            respuesta = input("Escribe 'si', 'mayor' o 'menor': ").lower()

            while respuesta not in ["si", "mayor", "menor"]:
                print("Respuesta inválida. Escribe 'si', 'mayor' o 'menor'.")
                respuesta = input("Escribe 'si', 'mayor' o 'menor': ").lower()
        else:  # Turno del usuario
            try:
                intento = int(input("Intenta adivinar el número: "))
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")
                continue

            if intento != numero_secreto:  # Solo dar pista si no ha acertado
                if intento < numero_secreto:
                    print("Pista: El número secreto es mayor.")
                else:
                    print("Pista: El número secreto es menor.")

            respuesta = "si" if intento == numero_secreto else "mayor" if intento < numero_secreto else "menor"

        if respuesta == "si":
            return True, intentos, numero_secreto  # Acertó (retorna numero_secreto siempre)
        elif respuesta == "mayor":
            limite_inferior = intento + 1
        else:  # respuesta == "menor"
            limite_superior = intento - 1
        vidas -= 1

    return False, intentos, numero_secreto  # No acertó (retorna numero_secreto siempre)

def pc_adivina():
    """El PC intenta adivinar el número del usuario."""
    limite_superior, vidas = obtener_dificultad()
    exito, intentos, _ = adivinar_numero(limite_superior, vidas, es_pc=True)  # No usamos numero_secreto

    if exito:
        print(f"¡Adiviné en {intentos} intentos!")
    else:
        print("¡Me quedé sin vidas! No pude adivinar tu número.") 

def usuario_adivina():
    """El usuario intenta adivinar el número generado por el PC."""
    limite_superior, vidas = obtener_dificultad()
    exito, intentos, numero_secreto = adivinar_numero(limite_superior, vidas)

    if exito:
        print(f"¡Adivinaste en {intentos} intentos!")
    else:
        print(f"Te quedaste sin vidas. El número era {numero_secreto}.")

# Bucle principal del juego
while True:
    print("\nBienvenido al Juego de Adivinanzas!")
    print("1. PC Adivina")
    print("2. Usuario Adivina")
    print("3. Finalizar")

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
    else:
        print("Fin del juego. ¡Gracias por jugar!")
        break
