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
    print(f"\nEl numero {n1} es IMPAR\n")
    print(f"Numeros IMPARES antes de {n1}")
    #Aqui le pedi al for que Empezara en 1, terminara en n1 y aumentara 2 veces
    for i in range(1,n1,2):
        print(f"{i}",end=" ")
else:
    print(f"\nEl numero {n1} es PAR\n")
    print(f"Numeros PARES antes de {n1}")
    #Aqui le pedi al for que Empezara en 2, terminara en n1 y aumentara 2 veces
    for i in range(2,n1,2):
        print(f"{i}",end=" ")
input("\nPresione ENTER para cerrar el programa ")