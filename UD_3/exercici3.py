#Part1

f = open("prueba.txt", "w")
f.write("Primera línia\n")
f.close()

f = open("prueba.txt", "w")
f.write("Segona línia\n")
f.close()

#En mode w, cada volta que obris el fitxer es borra el que hi havia i només es guarda l’última línia que escrius.

#Part 2

try:
    f = open("prueba.txt", "x")  
    f.write("Tercera línia\n")
    f.close()
    print("Creat amb mode x")
except FileExistsError:
    print("Error: el fitxer ja existeix")

#quan obris el fitxer amb mode x, Python el vol crear només si encara no existeix. Si ja estava creat d’abans, dona error

#Part3

f = open("prueba.txt", "a")
f.write("Quarta línia\n")
f.close()

f = open("prueba.txt", "a")
f.write("Cinquena línia\n")
f.write("Sisena línia\n")
f.close()

f = open("prueba.txt", "r")
print("Contingut actual de prueba.txt:")
print(f.read())
f.close()

#Part4

try:
    f = open("prueba_inexistent.txt", "r") 
    text = f.read()
    f.close()
    print(text)
except FileNotFoundError:
    print("Error: FileNotFoundError al llegir un fitxer que no existeix")

#si obris amb r un fitxer que no existeix, ix un error perquè no el pot llegir.