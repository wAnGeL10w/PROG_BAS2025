#FUNCION PARA OBTENER EL AREA
def area_c(v1):
    if v1<=0:
        print("El area de un circulo NO pueded ser negativa\n")
        print("Vuelva a ejecutar el programa")
    area=3.1416*(v1**2)
    return area
#FUNCION PARA OBTENER LA CIRCUNFERENCIA
def circunf(v1):
    if v1<=0:
        print("El area de un circulo NO pueded ser negativa\n")
        print("Vuelva a ejecutar el programa")
    diam=3.1416*(2*v1)
    return diam

print("Hola, Bienvenido\n")
import time
time.sleep(2)
#Peticion del numero al usuario 
n1=float(input("Escribe el radio: "))
#Aqui lo que hice fue llamara a las funciones y asi ya solo escribo y modifico el valor de entrada
#como n1
print(f"\nEl area del circulo es: {area_c(n1)}")
print(f"\nLa circunferencia del circulo es: {circunf(n1)}")
input("\nPresione ENTER para cerrar el programa ")