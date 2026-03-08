notes = [5, 7, 9, 4, 6, 3, 1, 8, 2, 10]

print("Totes les notes:")
for nota in notes:
    print(nota)

print("\nNotes aprovades (>=5):")
for nota in notes:
    if nota >= 5:
        print(nota)

aprovats = 0
suspesos = 0
for nota in notes:
    if nota >= 5:
        aprovats += 1
    else:
        suspesos += 1

print("\nTotal aprovats:", aprovats)
print("Total suspesos:", suspesos)