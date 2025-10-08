# CuentaTexto.py

# Pedir al usuario que ingrese un texto
texto = input("Introduce un texto: ")

# Contar cuántas veces aparece la palabra "Python"
# Se distingue mayúsculas/minúsculas según el ejemplo
contador = 0
palabra = "Python"
long_palabra = len(palabra)

# Recorrer el texto con subcadenas
for i in range(len(texto) - long_palabra + 1):
    if texto[i:i+long_palabra] == palabra:
        contador += 1

# Mostrar el resultado
print(f'La palabra "Python" aparece {contador} veces en el texto.')
