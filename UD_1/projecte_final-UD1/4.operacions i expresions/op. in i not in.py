fruites = ["pomes", "taronjes", "fresons"]

print("fruites:", fruites)

fruta = input("buscar fruita: ")

if fruta in fruites:
    print("Sí, es troba a la llista")
if fruta not in fruites:
    print("No, no es troba a la llista")
