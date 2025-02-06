print("Hola, Bienvenido\n")
import time
time.sleep(2)
n1=int(input("Escribe el numero a obtener su factorial: "))
#Valido para que si es 0, no le permita al usuario ver el calculo
if n1<0:
    print ("\nSu factorial debe ser POSITIVO")
else:
    #Como ya se validó, ya se puede realizar el proceso  
    fact=1
    for i in range (1,n1+1):
        #Lo que se hace aquí es que fact=1 se ira acumulado pero por medio de una multiplicacion
        #Y se ira multiplicando por cada posición de i. El rango es de 1 a n1+1 porque se está
        #multiplicando, si fuera con otro poceso se podria hacer de 0 a n1
        fact*=i
        #Ejemplo fact=1
        #fact=1*i (donde i=1)   entonces fact=1
        #fact=1*i (donde i=2 y fact vuelve a valer 1 pero se guardó el valor anterior) entoncces fact=2
        #El proceso se repite la cantidad de veces se repite acorde al valor de n1
    print(f"\nEl factorial de {n1} es: {fact}")
input("\nPresione ENTER para cerrar el programa ")