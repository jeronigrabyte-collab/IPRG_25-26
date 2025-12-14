elements = ["poma", "taronja", "poma", "fresa"]
seleccio = None #variable temporal

try:
    pos = int(input("Introdueix una posició (0-3): "))
    seleccio = elements[pos]
    print(f"L'element a la posició {pos} és: {seleccio}")

except ValueError:
    print("Error: has d'introduir un número")

except IndexError:
    print("Error: la posició no existeix")

finally:
    print("Intent completat.")
    print(f"Longitud de la llista: {len(elements)}")
    print(f"Valor de seleccio: {seleccio}")
