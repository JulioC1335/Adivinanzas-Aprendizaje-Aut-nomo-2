###Realizado Por Julio Cisneros 
###Juego de Adivinanzas (Adivinar el número)

**Inicio del Proyecto**: 6/2/2024

**Fin del Proyecto**:6/30/2024

**Problema**: Desarrollar el juego de Adivina  (el computador deberá adivinar el numero del usuarioz

**Propósito del Proyecto**: Implementar todos los conocimientos adquiridos en la asignatura de Lógica de la Programación para desarrollar un juego en Python.

**Tenemos dos modos de juego**

**Modo Usuario Adivina: **El usuario intenta adivinar un número secreto generado por la computadora.

**Modo PC Adivina: **La computadora intenta adivinar el número que el usuario está pensando



**ESRTRUCTURA DEL JUEGO**

**import random:** importa la biblioteca random, que proporciona funciones para generar números aleatorios.
````
import random
````




**Niveles de dificultad:**

Nivel 1: Números del 1 al 50, con 5 vidas.
Nivel 2: Números del 1 al 100, con 7 vidas.
Nivel 3: Números del 1 al 200, con 10 vidas.
Al elegir la dificultad, verás este mensaje:
````
¿Qué modo de dificultad quieres? (1, 2 o 3)
1: 1 al 50  |  Vidas: 5
2: 1 al 100 |  Vidas: 7
3: 1 al 200 |  Vidas: 10``
````
**Modo Usuario Adivina:**

En este modo, recibirás pistas indicando si el número secreto es mayor o menor que tu intento.
````

def usuario_adivina():
    """El usuario intenta adivinar el número generado por el PC."""
    limite_superior, vidas = obtener_dificultad()
    exito, intentos, numero_secreto = adivinar_numero(limite_superior, vidas)

    if exito:
        print(f"¡Adivinaste en {intentos} intentos!")
    else:
        print(f"Te quedaste sin vidas. El número era {numero_secreto}.")````


**Modo PC Adivina:**
En este modo, la computadora te preguntará si el número que estás pensando es mayor, menor o igual al número que ella propone.
````
def pc_adivina():
    """El PC intenta adivinar el número del usuario."""
    limite_superior, vidas = obtener_dificultad()
    exito, intentos, _ = adivinar_numero(limite_superior, vidas, es_pc=True)  

    if exito:
        print(f"¡Adiviné en {intentos} intentos!")
    else:
        print("¡Me quedé sin vidas! No pude adivinar tu número.") 
		
		
		````
**Logica principal del juego(Adivinar número)**
````
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

````
**Bucle del juego principal**
````

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
````

#Muchas gracias espero que lo disfruten
