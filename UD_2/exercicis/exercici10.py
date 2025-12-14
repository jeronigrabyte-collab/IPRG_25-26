elements = ["poma", "pera", "taronja", "plàtan"]
seleccio = None #variable temporal

try:
    pos = int(input("Introdueix una posició (0-3): "))
    
    #asserció
    assert 0 <= pos <= 3
    
    seleccio = elements[pos]
    print(f"L'element a la posició {pos} és: {seleccio}")

#captura d'excepcions
except ValueError:
    print("Error: has de posar un número enter")
except AssertionError:
    print("Error: la posició ha d'estar entre 0 i 3.")
    
    print("✅ Comprovació finalitzada.")
    print(f"Longitud de la llista: {len(elements)}")
    print(f"Selecció reiniciada a: {seleccio}")
