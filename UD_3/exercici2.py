def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r") as f:
            return f.read() + " "
    except FileNotFoundError:
        print(f"Error: El fitxer {nom_fitxer} no existeix")
        return ""

def concatenar_fitxers():
    fitxer1 = input("Nom del primer fitxer: ")
    fitxer2 = input("Nom del segon fitxer: ")
    fitxer3 = input("Nom del tercer fitxer: ")
    fitxer_final = input("Nom del fitxer final: ")
    
    contingut = ""
    contingut += llegir_fitxer(fitxer1)
    contingut += llegir_fitxer(fitxer2)
    contingut += llegir_fitxer(fitxer3)
    
    with open(fitxer_final, "w") as f:
        f.write(contingut.strip())
    
    print(f"\nFitxers concatenats en {fitxer_final}")

concatenar_fitxers()