#Creamos una funcion para solo mandarla a llamar y retornar si es o no primo
def num_primo(v1):
    #No puede haber numeros primos antes del 1 o el 1, asi que los descartamos con el condicional
    if v1<=1:
        print("El numero NO puede ser primo")
        return False
    for i in range(2,v1):
        #Validamos que el numero sea divisible entre 2 hasta el numero buscado. Si es divisible
        #NO ES PRIMO
        if v1%i==0:
            return False
    #Si no es divisible por ninguno entonces SI ES PRIMO    
    return True
print("Hola, Bienvenido\n")
import time
time.sleep(2)

n1=int(input("Escribe un numero: "))
#Mandamos a llamar la funcion y ejecutamos el codigo
if num_primo(n1):
    print(f"\nEl numero {n1} ES PRIMO")
else:
    print(f"\nEl numero {n1} NO ES PRIMO")
#Validacion para SALILR
input("\nPresione ENTER para cerrar el programa ")