fitxer1 = input("Introdueix el nom del primer fitxer: ")
fitxer2 = input("Introdueix el nom del segon fitxer: ")
fitxer3 = input("Introdueix el nom del tercer fitxer: ")

fitxer_final = input("Introdueix el nom del fitxer final: ")

contingut_total = ""

try:
    f1 = open(fitxer1, "r")
    contingut_total = contingut_total + f1.read() + " "
    f1.close()
    print("Fitxer 1 llegit correctament")
except:
    print("Error: El fitxer " + fitxer1 + " no existeix")

try:
    f2 = open(fitxer2, "r")
    contingut_total = contingut_total + f2.read() + " "
    f2.close()
    print("Fitxer 2 llegit correctament")
except:
    print("Error: El fitxer " + fitxer2 + " no existeix")

try:
    f3 = open(fitxer3, "r")
    contingut_total = contingut_total + f3.read() + " "
    f3.close()
    print("Fitxer 3 llegit correctament")
except:
    print("Error: El fitxer " + fitxer3 + " no existeix")

fitxer_nou = open(fitxer_final, "w")
fitxer_nou.write(contingut_total)
fitxer_nou.close()

print("\nFitxers concatenats correctament en " + fitxer_final)