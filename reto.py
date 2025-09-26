saldo = 500

print("Bienvenido al cajero automático")
print("Saldo inicial:", saldo)

while True:
    print("\n1. Retirar dinero")
    print("2. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = int(input("Ingrese el monto a retirar: "))

        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        else:
            if monto > saldo:
                print("Saldo insuficiente.")
            else:
                if monto % 10 != 0:
                    print("El monto debe ser múltiplo de 10.")
                else:
                    saldo -= monto
                    print("Retiro exitoso. Nuevo saldo:", saldo)

    elif opcion == "2":
        print("Gracias por usar el cajero. Hasta luego.")
        break
    else:
        print("Opción no válida.")
