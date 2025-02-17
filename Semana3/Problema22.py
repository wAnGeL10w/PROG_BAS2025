#Importamos esta libreria ya que nos permite trabajar con numeros aleatorios
import random

def dado():
    #Nos permite generar un numero del 1 al 6 (las caras de un dado)
    #Asl escribir random.radiant(a,b) le damos el rango de numeros que queremos
    return random.randint(1, 6)

def moneda():
    #Nos permite seleccionar entre cara o cruz
    #Al escribir random.choice("","") le decimos que queremos que nos seleccione (choice) alguno de los
    #Valores introducidos
    return random.choice(["Cara", "Cruz"])

# Mensaje de bienvenida
print("Hola, Bienvenido\n")
import time
time.sleep(2)

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Lanzar un dado")
    print("2. Lanzar una moneda")
    print("3. Salir")
    
    op=int(input("\nSelecciona una opción: "))

    if op==1:
        print(f"El dado cayó en: {dado()}")
    elif op==2:
        print(f"La moneda cayó en: {moneda()}")
    elif op==3:
        break
    else:
        print("Opción INVÁLIDA, Vuelva a ejecutar el programa.")

input("\nPresiona ENTER para cerrar el programa.")
