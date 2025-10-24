# ListaInvertida.py

# Pedir nombres separados por comas
nombres = input("Introduce nombres separados por comas: ")

# Convertir a lista y eliminar espacios
lista_nombres = [nombre.strip() for nombre in nombres.split(",")]

# Invertir la lista
lista_invertida = lista_nombres[::-1]

# Mostrar resultado
print("Lista invertida:", lista_invertida)
