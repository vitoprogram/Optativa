# Mini retos con funciones

# 1.Calcular el número mayor de una lista
def numero_mayor(lista):
    return max(lista)

# 2. Contar vocales en una cadena
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in cadena if letra in vocales)

# 3. Comprobar si un número es primo
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 4.Eliminarr elementos repetidos en una lista
def eliminar_repetidos(lista):
    return list(set(lista))

# 5. Implementar menú de operaciones básicas
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Saliendo del programa...")
            break

        if opcion in ["1", "2", "3", "4"]:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))

            if opcion == "1":
                print("Resultado:", a + b)
            elif opcion == "2":
                print("Resultado:", a - b)
            elif opcion == "3":
                print("Resultado:", a * b)
            elif opcion == "4":
                if b != 0:
                    print("Resultado:", a / b)
                else:
                    print("Error: No se puede dividir entre 0.")
        else:
            print("Opción no válida.")

# Ejemplos de uso
print("Número mayor:", numero_mayor([3, 7, 2, 9, 5]))
print("Cantidad de vocales:", contar_vocales("Hola mundo"))
print("¿Es primo 7?:", es_primo(7))
print("Lista sin repetidos:", eliminar_repetidos([1, 2, 2, 3, 3, 4]))

# El menú 
menu()

