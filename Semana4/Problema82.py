#Con esta libreria realizamos calculos matematicos
import statistics

print("Hola, Bienvenido\n")
import time
time.sleep(2)
#Pedimos al usuario los numeros mediante una lista
#La palabra reservada .split permite separar lo que escribamos
numeros=list(map(float, input("Ingrese números separados por espacio: ").split()))

# Calculamos la mediana y la moda
med=statistics.median(numeros)
#Esta opcion nos permite obtener la moda
#Try nos sirve por si hay varias modas, si hay mas de una imprime el texto
#Asi evita que el programa tebga error
try:
    moda=statistics.mode(numeros)
except statistics.StatisticsError:
    moda="No hay una única moda"

#Resultados
print(f"Mediana: {med}")
print(f"Moda: {moda}")

input("Presione ENTER para cerrar el programa ")

