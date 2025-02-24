import time
import os

#Declaramos un diccionario con las tasas de cambio
tasas = {
    "USD": {"EUR": 0.92, "MXN": 17.05},
    "EUR": {"USD": 1.09, "MXN": 18.50},
    "MXN": {"USD": 0.059, "EUR": 0.054}
}

print("Conversor de Moneda ")
print("Monedas disponibles: USD, EUR, MXN")

#Solicitamos la moneda de origen y destino
#La palabra reservada .upper() convierte el texto a mayusculas
moneda_i=input("Ingrese la moneda de origen: ").upper()
moneda_c=input("Ingrese la moneda de destino: ").upper()

#Validacion de datos
#Si lo escrito en MONEDA esta en tasas y si la CONVERSION esta en tasas[MONEDA]
if moneda_i in tasas and moneda_c in tasas[moneda_i]:
    cant=float(input(f"Ingrese la cantidad en {moneda_i}: "))
    if cant<0:
        print("La cantidad no puede ser negativa.")
        time.sleep(2)
        os.system('cls')
    else:
        conversion=cant*tasas[moneda_i][moneda_c]
        print(f" {cant} {moneda_i} equivale a {conversion:.2f} {moneda_c} 💱")
else:
    print("Conversión no disponible.")

input("Presione ENTER para cerrar el programa ")
