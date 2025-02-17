#Programa para determinar si el año es bisiesto

#Bienvenida para el USUARIO
print("Hola, Bienvenido\n")
import time
time.sleep(2)

#Peticion del año al usuario
año=int(input("Escribe un año: "))

if año%1==0 and año>0:
    if (año%4==0 and año%100!=0) or año%400==0:
        print(f"\nEl año {año} es BISIESTO")
    else:
        print(f"\nEl año {año} NO es BISIESTO")
else:
    print(f"\nEl año {año} es INCORRECTO, vuelve a ejecutar el programa")
    
input("\nPresione ENTER para cerrar el programa ")