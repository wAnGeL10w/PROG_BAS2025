import math
import cmath

def EcuCuad(a,b,c):
    if a==0:
        return "Ecuacion NO cuadratica"
    D=b**2-4*(a*c)
    if D >= 0:
        r1=(-b + math.sqrt(D)) / (2 * a)
        r2=(-b - math.sqrt(D)) / (2 * a)
    else:
        r1=(-b + cmath.sqrt(D)) / (2 * a)
        r2=(-b - cmath.sqrt(D)) / (2 * a)
    return r1,r2

print("Hola, Bienvenido\n")
import time
time.sleep(2)

n1=float(input("Ingrese el coeficiente a: "))
n2=float(input("Ingrese el coeficiente b: "))
n3=float(input("Ingrese el coeficiente c: "))

raices= EcuCuad(n1,n2,n3)
print("Las soluciones son: ",raices[0], "  y ", raices[1])

input("Presione ENTER para cerrar el programa ")
