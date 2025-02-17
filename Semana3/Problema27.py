#Con esta funcion calcularemos las longitudes
def longitud(v1, u_inc, u_fin):
    un={
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "inch": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mile": 1609.34
    }
    #Verificacion de unidades
    if u_inc in un and u_fin in un:
        #Permite cancelar factores y devolver la unidad deseada
        return v1*(un[u_fin]/un[u_inc])
    else:
        #En caso de error, no se devolvera nada
        return None

#Con esta funcion calcularemos los pesos
def pesos(v1,u_inc, u_fin):
    un={
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495
    }
    #verificaacion de unidades
    if u_inc in un and u_fin in un:
        #Permite cancelar factores y devolver la unidad deseada
        return v1*(un[u_fin]/un[u_inc])
    else:
        #En caso de error, no se devolvera nada
        return None

# Mensaje de bienvenida
print("Hola, Bienvenido\n")
import time
time.sleep(2)
print("Selecciona el tipo de conversión:")
print("1. Longitud")
print("2. Peso")

opc=int(input("Ingrese una opción (1-2): "))

res=None
if opc in [1, 2]:
    can=float(input("Ingrese el valor a convertir: "))

    if opc==1:
        #Longitud
        print("Unidades disponibles: m, km, cm, mm, inch, ft, yd, mile")
        uni=input("Ingrese la unidad de origen: ").strip().lower()
        unif=input("Ingrese la unidad de destino: ").strip().lower()
        res=longitud(can, uni, unif)

    elif opc == 2:
        #Peso
        print("Unidades disponibles: kg, g, mg, lb, oz")
        uni=input("Ingrese la unidad de origen: ").strip().lower()
        unif=input("Ingrese la unidad de destino: ").strip().lower()
        res= pesos(can, uni, unif)

    if res is not None:
        print(f"{can} {uni} equivale a {res:.4f} {unif}")
    else:
        print("Unidades inválidas o conversión no soportada.")

else:
    print("Opción no válida.")

input("\nPresione ENTER para cerrar el programa ")
