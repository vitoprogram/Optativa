# SumaSecuencia.py

# Pedir al usuario una secuencia de números separados por espacios
numeros = input("Introduce una secuencia de números separados por espacios: ")

# Convertir lacadena en una lista de números
lista_numeros = [float(num) for num in numeros.split()]

# Calcular la suma total
suma_total = sum(lista_numeros)

# Mostrar el resultado
print("La suma total es:", suma_total)
