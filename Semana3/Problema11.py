#Declaración de unq funcion para determinar la palabra palindroma
def p_palindroma(v1):
    #La propiedad .lower() convierte la cadena a letras minusculas
    #La propuedad .replace("","") hace que lo que esta en las primeras comillas se cambie por lo que
    #esta en las segundas comillas. Como no hay nada en las segundas comillas, se eliminan los espacios
    v1 = v1.lower().replace(" ", "")
    #Al escribir v1[::-1] signidca que [: ] donde empieza [:: ] donde va a terminar [::-1] espacios
    #Que se va a recorrer. Cuandoe es -1 significa que se recorre de derecha a izquierda
    return v1 == v1[::-1]  # Comparar con su inversa


print("Hola, Bienvenido\n")
import time
time.sleep(2)

#Proceso
texto=str(input("Ingresa una cadena: \n"))
if p_palindroma(texto):
    print("La cadena es un palíndromo\n")
else:
    print("La cadena no es un palíndromo\n")
input("Presione ENTER para cerrar el programa ")