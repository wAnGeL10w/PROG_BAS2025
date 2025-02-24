def InteresCompuesto(v1,v2,v3):
    if v1<0 or v2<0 or v3<0:
        print("Los valores no pueden ser negativos")
        return None
    else:
        IntCom1=v1*(1+v2)**v3
        IntCom2=v1*(1+v2/12)**(v3*12)
        return IntCom1,IntCom2

print("Hola, Bienvenido\n")
import time
time.sleep(2)

Cap_I=float(input("Ingrese el capital inicial: "))
T_Int=float(input("Ingrese la tasa de interes anual: %"))/100
Tiem=float(input("Ingrese el tiempo en años: "))

res=InteresCompuesto(Cap_I,T_Int,Tiem)

if res==None:
    print("Error")
else:
    print("El capital final con interes compuesto anual es: ",res[0])
    print("El capital final con interes compuesto mensual es: ",res[1])

input("Presione ENTER para cerrar el programa ")