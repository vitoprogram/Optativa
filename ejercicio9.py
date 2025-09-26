secreto = 7
adivina = 0

print("Adivina el número secreto entre 1 y 10")

while adivina != secreto:
    adivina = int(input("Introduce tu número: "))

    if adivina == secreto:
        print("¡Correcto! Has adivinado el número.")
    else:
        if adivina > secreto:
            print("Muy alto.")
        else:
            print("Muy bajo.")
