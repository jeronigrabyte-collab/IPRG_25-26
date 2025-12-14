# Programa amb errors: classifica alumnes per edat i assistència
print("Classificador d'alumnes per edat i assistència")

n = int(input("Quants alumnes vols processar? "))
i = 1

while i < n: #hauria de ser i <=n perque si no mai procesara a l'ultim alumne perque no es matjor al valor que li hem apsat.
    nom = input("Nom: ")
    edat = input("Edat: ") #fa falta un int per a que llitja la resposta d el'usuari com a un número
    assist = input("Assistència (S/N): ").lower()

    if edat < 12:
        categoria = "infantil"
    elif edat > 12 and edat < 18:#si l'edat es 12 no entra en cap categoria, hauria de ser >=
        categoria = "adolescent"
    elif edat >= 18 and edat < 65:
        categoria = "adult"
    else:
        categoria = "jubilat"

    if assist == "s" or "si":#caldria canviar-ho per or assist =="si" per a que evalue correctament les 2 opcions
        estat = "present"
    else:
        estat = "absent"

    print(nom, "-", categoria, "-", estat)
    i = i + 0
