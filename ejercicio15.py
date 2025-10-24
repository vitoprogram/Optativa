# BuscaNumeros.py

numeros = []

# Pedir números hasta que el usuario escriba 0
while True:
    n = int(input("Escribe un número (0 para terminar): "))
    if n == 0:
        break
    numeros.append(n)

# Pedir número a buscar
buscar = int(input("¿Qué número quieres buscar?: "))

# Buscar posiciones
posiciones = [i for i, num in enumerate(numeros) if num == buscar]

# Mostrar resultado
if posiciones:
    print(f"El número {buscar} aparece en las posiciones: {posiciones}")
else:
    print(f"El número {buscar} no aparece en la lista.")
