print("CALCULADORA D'IMC")

pes = float(input("Introdueix el teu pes (en kg): "))
alçada = float(input("Introdueix la teua alçada (en metres): "))

imc = pes / (alçada ** 2)

print(f"El teu IMC és: {imc:.2f}")
if imc < 18.5:
    print("Estàs per davall del pes saludable.")
elif imc >= 18.5 and imc <= 24.9:
    print("Tens un pes saludable. Perfecte!")
else:
    print("Estàs en sobreeiximent de pes.")