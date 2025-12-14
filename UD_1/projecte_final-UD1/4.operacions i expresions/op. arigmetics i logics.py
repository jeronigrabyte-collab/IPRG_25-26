x = 10
y = 5

print("operacions:")

suma = x + y
resta = x - y
multiplicacion = x * y
divisio = x / y
modul = x % y

print(f"Suma: {x} + {y} = {suma}")
print(f"Resta: {x} - {y} = {resta}")
print(f"Multiplicación: {x} * {y} = {multiplicacion}")
print(f"Divisió: {x} / {y} = {divisio}")
print(f"Modul: {x} % {y} = {modul}")

print("comparacions:")
if x > y:
    print(f"{x} es més gran que {y}")
else:
    print(f"{x} NO es més gran que {y}")

if x == y:
    print(f"{x} es igual a {y}")
else:
    print(f"{x} NO es igual a {y}")

print("operadors lògics:")
if x > y and x % 2 == 0:
    print(f"{x} es més gran que {y} i el módul de {x} es 0")
else:
    print("No es cumplix la condició")