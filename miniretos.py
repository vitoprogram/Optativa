# Mini retos en Python

nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]

# Suma de todos
suma_total = 0
for n in nums:
    suma_total += n
print("Suma de todos:", suma_total)

# Cuál es el máximo
maximo = nums[0]
for n in nums:
    if n > maximo:
        maximo = n
print("Máximo:", maximo)

# Contar ocurrencias de un número
num = int(input("Introduce un número para contar cuántas veces aparece: "))
contador = 0
for n in nums:
    if n == num:
        contador += 1
print(f"El número {num} aparece {contador} veces.")

# Calcular la media sin usar sum()
suma = 0
for n in nums:
    suma += n
media = suma / len(nums)
print("Media de la lista:", media)

# Crear una lista solo con los pares
pares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
print("Lista de números pares:", pares)

# Hallar max(nums) - min(nums) usando for
mayor = nums[0]
menor = nums[0]
for n in nums:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n
print("Diferencia entre máximo y mínimo:", mayor - menor)

# Pedir un número y mostrar el primer índice donde aparece (o -1 si no está)
num_buscado = int(input("Introduce un número para buscar su primer índice: "))
indice = -1
for i in range(len(nums)):
    if nums[i] == num_buscado:
        indice = i
        break
print("Primer índice donde aparece:", indice)
