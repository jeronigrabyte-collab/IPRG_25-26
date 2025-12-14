import json

nom_fitxer = "dades_exercici.json"

dades_inicials = {
    "Nom": "Jeroni",
    "Edat": 33,
    "Nota": 10,
    "Assignatures": ["IPRG", "SEX", "PI"]
}

with open(nom_fitxer, "w") as f:
    json.dump(dades_inicials, f, indent=4)

print(f"Fitxer '{nom_fitxer}' creat amb dades inicials.\n")


try:
    with open(nom_fitxer, "r") as f:
        estudiant = json.load(f)
    
    print(f"Dades actuals: {estudiant}")
    
    nova_assignatura = input("\nAfegeix una nova assignatura: ")
    
    estudiant["Assignatures"].append(nova_assignatura)
    

    with open(nom_fitxer, "w") as f:
        json.dump(estudiant, f, indent=4)

    print(f"\nDades guardades correctament en '{nom_fitxer}'.")
    
    print("ambtingut final de la llista d'assignatures:", estudiant["Assignatures"])


except FileNotFoundError:
    print(f"El fitxer '{nom_fitxer}' no existeix.")
except json.JSONDecodeError:
    print(f"El fitxer no té un format JSON vàlid (està corrupte o buit).")
except Exception as e:
    print(f"Error inesperat: {e}")