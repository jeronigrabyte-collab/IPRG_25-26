numero = int(input("introdueix un número, per a finalitzar escriu 0: "))
comptador = 0

while numero != 0:
    if numero > 0:
        comptador = comptador + 1

    numero = int(input("Introudeix un número, per a finalitzar escriu 0: "))

print("Has introduit els seguents numeros positius:")
print(comptador)