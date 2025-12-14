import math

def calcular_area_cercle(radi):
    area = math.pi * radi ** 2
    return area

radi = float(input("Introduce el radio del círculo: "))

area = calcular_area_cercle(radi)

print(f"Radi: {area:.2f}")