print("Hola, Bienvenido\n")
#Imorte una libreria que permite controlar tiempos en el programa
import time
#Esta funcion genera una pausa y el numero escrito en "()" sera la cantida en segundos de la pausa
time.sleep(2)
#Esta forma de escribir un variable permite que el usuario ingrese una cantidad despues del texto
n1=float(input("Escribe un numero: "))
n2=float(input("Escribe un numero: "))
#CALCULOS
suma=(n1)+(n2)
resta=(n1)-(n2)
multi=(n1)*(n2)
divi=(n1)/(n2)
print(" \n")
#IMPRESION DE RESULTADOS
#La letra f antes de las comillas permite imprimir valores de variables numericas, las cuales
#deveran ser escritas en corchetes "{}"
print(f"La suma de {n1} y {n2} es: {suma}")
print(f"La resta de {n1} y {n2} es: {resta}")
print(f"La multiplicacion de {n1} y {n2} es: {multi}")
print(f"La division de {n1} y {n2} es: {divi}\n")
input("Presione ENTER para cerrar el programa ")