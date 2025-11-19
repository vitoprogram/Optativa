# MiniArcade.py
import random
import time

# ------------------------------
# Función para pedir opción válida
# ------------------------------
def pedir_opcion():
    while True:
        op = input("Elige una opción: ").strip()
        if op in {"0", "1", "2", "3", "4"}:
            return op
        print("Opción no válida. Intenta de nuevo.")


# ------------------------------
# Juego 1: Piedra Papel Tijera
# ------------------------------
def juego_ppt():
    print("\n--- Piedra, Papel o Tijera ---")
    opciones = ["piedra", "papel", "tijera"]

    while True:
        user = input("Elige piedra, papel o tijera (o enter para salir): ").lower().strip()
        if user == "":
            print("Saliendo del juego...")
            return
        if user not in opciones:
            print("Opción inválida.")
            continue

        bot = random.choice(opciones)
        print(f"El bot eligió: {bot}")

        if user == bot:
            print("Empate.")
        elif (user == "piedra" and bot == "tijera") or \
             (user == "tijera" and bot == "papel") or \
             (user == "papel" and bot == "piedra"):
            print("¡Ganaste!")
        else:
            print("Perdiste.")


# ------------------------------
# Juego 2: Adivina el número
# ------------------------------
def juego_adivina():
    print("\n--- Adivina el Número ---")
    print("Dificultad: 1) Fácil (1-20)   2) Normal (1-50)   3) Difícil (1-100)")

    rangos = {"1": 20, "2": 50, "3": 100}

    diff = input("Elige dificultad: ").strip()
    if diff not in rangos:
        print("Dificultad no válida → modo Fácil")
        limite = 20
    else:
        limite = rangos[diff]

    numero = random.randint(1, limite)
    intentos = 5
    inicio = time.time()

    print(f"Adivina el número entre 1 y {limite}. Tienes {intentos} intentos.")

    while intentos > 0:
        try:
            x = int(input("Tu número: "))
        except:
            print("Introduce un número válido.")
            continue

        intentos -= 1

        if x == numero:
            tiempo = round(time.time() - inicio, 2)
            print(f"¡Correcto! Lo adivinaste en {tiempo} segundos.")
            return

        elif x < numero:
            print("Más ↑")
        else:
            print("Menos ↓")

        print(f"Intentos restantes: {intentos}")

    print(f"Fallaste. El número era {numero}.")


# ------------------------------
# Juego 3: Cálculo mental exprés
# ------------------------------
def juego_calculo_mental_expres(preguntas=8, tiempo_total=35):
    print("\n--- Cálculo Mental Exprés ---")
    print(f"Tienes {tiempo_total} segundos para responder {preguntas} preguntas.")
    time.sleep(1)

    inicio = time.time()
    aciertos = 0

    for i in range(1, preguntas + 1):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(["+", "-"])
        correcto = a + b if op == "+" else a - b

        print(f"\nPregunta {i}: {a} {op} {b} = ?")

        # Revisar tiempo
        if time.time() - inicio > tiempo_total:
            print("⏳ Se acabó el tiempo.")
            break

        try:
            resp = int(input("Respuesta: "))
        except:
            print("Respuesta inválida.")
            continue

        if resp == correcto:
            aciertos += 1
            print("✔ Correcto")
        else:
            print(f"✘ Incorrecto. Era {correcto}")

    print(f"\nPuntuación final: {aciertos}/{preguntas}")
    return aciertos


# ------------------------------
# Juego 4: Eco invertido
# ------------------------------
def juego_eco_invertido():
    print("\n--- Eco Invertido ---")
    print("Escribe texto. Enter vacío para salir.")

    while True:
        txt = input("> ")
        if txt == "":
            print("Fin del eco.")
            return

        invertida = txt[::-1]
        vocales = sum(1 for c in txt.lower() if c in "aeiouáéíóú")
        print(f"Invertida: {invertida}")
        print(f"Caracteres: {len(txt)} | Vocales: {vocales}")


# ------------------------------
# MAIN del programa
# ------------------------------
def main():
    print("Bienvenido/a al Mini Arcade 👾")

    while True:
        print("\n=== MINI ARCADE ===")
        print("1) Piedra, Papel o Tijera")
        print("2) Adivina el número")
        print("3) Juego cálculo mental")
        print("4) Eco invertido")
        print("0) Salir")

        opcion = pedir_opcion()

        if opcion == "1":
            juego_ppt()
        elif opcion == "2":
            juego_adivina()
        elif opcion == "3":
            juego_calculo_mental_expres()
        elif opcion == "4":
            juego_eco_invertido()
        elif opcion == "0":
            print("¡Hasta luego!")
            break

        time.sleep(0.8)


# ------------------------------
# Bloque protector
# ------------------------------
if __name__ == "__main__":
    main()
