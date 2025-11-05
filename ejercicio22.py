import random
import time

def adivinar_numero():
    print("Bienvenido al juego de Adivinar el Número")
    time.sleep(1)
    print("Estoy pensando en un número entre 1 y 100...")
    time.sleep(1)

    numero_secreto = random.randint(1, 100)
    intentos = 0
    inicio = time.time()

    while True:
        try:
            intento = int(input("Adivina el número: "))
            intentos += 1

            diferencia = abs(intento - numero_secreto)

            if intento < numero_secreto:
                print("Demasiado bajo.")
            elif intento > numero_secreto:
                print("Demasiado alto.")
            else:
                fin = time.time()
                duracion = round(fin - inicio, 2)
                print(f"¡Correcto! El número era {numero_secreto}.")
                print(f"Has tardado {intentos} intentos y {duracion} segundos.")
                break

            # Pistas matemáticas
            if diferencia > 7:
                print("Frío ❄️")
            elif diferencia <= 3:
                print("Caliente 🔥")

        except ValueError:
            print("Por favor, introduce un número válido.")

# Ejecutar el juego
adivinar_numero()
