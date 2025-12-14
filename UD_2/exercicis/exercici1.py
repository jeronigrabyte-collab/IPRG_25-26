temperatura= float(input("Temperatura en celsius: "))
nuvolat= input("Esta nuvolat? (si/no): ").lower()

if temperatura < 0:
    print("Fa un fred polar!")

elif 0 <= temperatura <=15:
    if nuvolat == "si":
        print("Fa fred i el dia esta trist.")
    else:
        print("Fa fresqueta però el sol alegra el dia")

elif 16 <= temperatura <= 25:
    if nuvolat == "si":
        print("Temperatura agradable, però potser ploga")
    else:
        print("Dia perfecte per a eixir a passejar!")

elif 26 <= temperatura <= 35:
    print("Fa calor, millor busca l'ombra")

elif temperatura > 35:
    if nuvolat =="si":
        print("calor i humitat...una combinació infernal!")
    else:
        print("Fa una calor que fon les pedres!")
