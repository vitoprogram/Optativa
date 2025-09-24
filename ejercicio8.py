n1 = float(input("Introduce la primera nota: "))
n2 = float(input("Introduce la segunda nota: "))
n3 = float(input("Introduce la tercera nota: "))

if n1 <= 4 and n2 <= 4 and n3 <= 4:
    final = 0
elif n1 > 4 and n2 > 4 and n3 > 4:
    final = (0.3 * n1) + (0.2 * n2) + (0.5 * n3)
else:
    final = 2

print("La nota final es:", final)