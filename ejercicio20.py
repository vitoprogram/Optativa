# Calcular el máximo común divisor
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Funcion para comprobar si un número es primo
def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Programa principal
if __name__ == "__main__":
    # Calcular MCD de 20 y 12
    resultado_mcd = mcd(20, 12)
    print(f"El MCD de 20 y 12 es: {resultado_mcd}")

    # Mostrar números primos del 1 al 50
    print("Números primos del 1 al 50:")
    for i in range(1, 51):
        if esPrimo(i):
            print(i, end=" ")
