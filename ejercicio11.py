# MayorMenor.py

# Pedir al usuario cuántos números va a introducir
n = int(input("Dime cuántos números vas a introducir: "))

# Inicializar variables
mayor = None
menor = None

print(f"Escribe {n} números:")

# Bucle para leer los números
for i in range(n):
    num = int(input())
    
    # En la primera iteración, inicializamos mayor y menor
    if i == 0:
        mayor = num
        menor = num
    else:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

# Mostrar resultados
print(f"El mayor es {mayor}")
print(f"El menor es {menor}")
