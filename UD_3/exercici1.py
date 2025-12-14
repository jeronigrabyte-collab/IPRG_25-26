nom = input("Introdueix el teu nom: ")
edat = input("Introdueix la teva edat: ")


fitxer = open("dades_usuari.txt", "w")
fitxer.write("Nom: " + nom + "\n")
fitxer.write("Edat: " + edat + "\n")
fitxer.close()

print("Dades guardades correctament!")

fitxer = open("dades_usuari.txt", "r")
contingut = fitxer.read()
print("\nContingut del fitxer:")
print(contingut)
fitxer.close()

nova_dada = input("\nIntrodueix una altra dada (per exemple, ciutat): ")
fitxer = open("dades_usuari.txt", "a")
fitxer.write(nova_dada + "\n")
fitxer.close()

print("Nova dada afegida!")

fitxer = open("dades_usuari.txt", "r")
contingut_final = fitxer.read()
print("\nContingut final del fitxer:")
print(contingut_final)
fitxer.close()

