#Creacion de una funcion para realizar el modulo
def modulo(v1,v2):
    #Hacemos esto porque en un futuro nos permite asignarle cualquier valor a ambos parametros
    return v1%v2

print("Hola, Bienvenido\n")
import time
time.sleep(2)
#Peticion del numero al usuario 
n1=int(input("Escribe un numero: "))

#Validacion del modulo
if modulo(n1,2)!=0:
    print(f"\nEl numero {n1} es IMPAR")
else:
    print(f"\nEl numero {n1} es PAR")
#Validacion de multiplos
v3=int(input("\nEscribe el numero multiplo: "))
#Asignamos al divisor el valor de v3 porque es el que el usuario quiere saber si es multiplo
if modulo(n1,v3)==0:
    print(f"\nEl numero {v3} ES multiplo de {n1}")
else:
    print(f"\nEl numero {v3} NO es multiplo de {n1}")
input("\nPresione ENTER para cerrar el programa ")