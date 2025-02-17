#Bienvenida para el USUARIO
print("Hola, Bienvenido\n")
import time
time.sleep(2)

#Este es mi primer arreglo. Utilice un arreglo porque hace mas sencillo el proceso, comparando
#sus posiciones y ver cual es mas grande
n1=0
numeros=[]
i=0

#Este proceso es solo para darle valores al arreglo unidimensional
for i in range(0,3,1):
    print("\nEscribe un numero: ")
    n1=float(input())
    numeros.append(n1)

#Ahora veremos cual de los 3 valores escritos es mayor
if numeros[0]>numeros[1] and numeros[0]>numeros[2]:
    print(f"El numero {numeros[0]} es el mayor")
else:
    if numeros[1]>numeros[2] and numeros[1]>numeros[0]:
        print(f"El numero {numeros[1]} es el mayor")
    else:
        print(f"El numero {numeros[2]} es el mayor")

input("\nPresione ENTER para cerrar el programa ")