#Esta libreria nos permite trabajar con cuestiones aleatorias
import random

#Lista de letras, caracteres y numeros
caracteres=["A","c","E","g","I","k","M","ñ","P","r","T","v","X","z","1", "2","3","4","5","6","7","8","9","0","*","#","$","%","&","!","?","@","+","-"]

def Contra(v1):
    #Se seleccionara un caracter de manera aleatoria
    #El apartado range nos permite seleccionar la cantidad de caracteres que queremos
    return ''.join(random.choice(caracteres) for _ in range(v1))

print("Hola, Bienvenido\n")
import time
time.sleep(2)

#Peticion de la cantidad de caracteres
cant=int(input("¿Cuántos caracteres quieres que tenga tu contraseña?: "))
#Proceso
if cant<1:
    print("\nNo se puede generar una contraseña con esa cantidad de caracteres")
else:
    print(f"\nTu contraseña es: {Contra(cant)}")

input("\nPresiona ENTER para cerrar el programa ")