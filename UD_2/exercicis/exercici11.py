import logging

# Configuració bàsica del sistema de logs
logging.basicConfig(
    level=logging.DEBUG,                      # Mostra tots els missatges (DEBUG o superiors)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format amb hora, nivell i missatge
    filename='operacions.log',                # Guarda les traçades en un fitxer
    filemode='w'                              # Sobreescriu el fitxer cada vegada que s’executa
)

#definició funcions matemàtiques

def suma(a, b):
    resultat = a + b
    logging.info(f"Suma: {a} + {b} = {resultat}")
    return resultat

def resta(a, b):
    resultat = a - b
    logging.info(f"Resta: {a} - {b} = {resultat}")
    return resultat

def multiplicacio(a, b):
    resultat = a * b
    logging.info(f"Multiplicació: {a} * {b} = {resultat}")
    return resultat

def divisio(a, b):
    try:
        resultat = a / b
        logging.info(f"Divisió: {a} / {b} = {resultat}")
        return resultat
    except ZeroDivisionError:
        logging.error(f"Error: intent de divisió per zero ({a} / {b})")
        print("No es pot dividir per zero")
        return None
    
#programa principal
logging.info("Programa iniciat")

num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

suma(num1, num2)
resta(num1, num2)
multiplicacio(num1, num2)
divisio(num1, num2)

logging.info("Programa finalitzat")
print("Operacions completades. Revisa el fitxer operacions.log")
