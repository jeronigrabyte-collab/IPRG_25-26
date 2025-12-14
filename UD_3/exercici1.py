def demanar_dades():
    nom = input("Introdueix el teu nom: ")
    edat = input("Introdueix la teva edat: ")
    return nom, edat

def guardar_fitxer(nom, edat):
    with open("dades_usuari.txt", "w") as fitxer:
        fitxer.write(f"Nom: {nom}\n")
        fitxer.write(f"Edat: {edat}\n")
    print("Dades guardades correctament!")

def llegir_fitxer():
    with open("dades_usuari.txt", "r") as fitxer:
        contingut = fitxer.read()
        print("\nContingut del fitxer:")
        print(contingut)

def afegir_dada():
    nova_dada = input("\nIntrodueix la teva ciutat: ")
    with open("dades_usuari.txt", "a") as fitxer:
        fitxer.write(f"{nova_dada}\n")
    print("Nova dada afegida!")

def mostrar_final():
    with open("dades_usuari.txt", "r") as fitxer:
        print("\nContingut final:")
        print(fitxer.read())

nom, edat = demanar_dades()
guardar_fitxer(nom, edat)
llegir_fitxer()
afegir_dada()
mostrar_final()
