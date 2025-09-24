# Pedir la nota al usuario
nota = float(input("Introduce una nota (0-10): "))

# Validar rango
if 0 <= nota <= 10:
    if nota < 5:
        print("Insuficiente")
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 8:
        print("Notable")
    elif nota < 9:
        print("Sobresaliente")
    else:  # nota entre 9 y 10 inclusive
        print("Sobresaliente")
else:
    print("Nota no válida")
