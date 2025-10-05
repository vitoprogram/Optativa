# Factura.py

total = 0.0  # Variable para acumular el total

while True:
    precio = float(input("Introduce el precio del producto (0 para terminar): "))
    if precio == 0:
        break
    total += precio  # Sumar el precio al total

# Mostrar el total con 2 decimales
print(f"El total de la factura es: {total:.2f} €")
