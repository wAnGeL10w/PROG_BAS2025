def vocal_cons(texto):
    #Con esto logramos identificar las vocales, ya sea mayusculas o minusculas
    voc = "aeiouAEIOU"
    #Contadores de las vocales y consonantes
    c_voc = 0
    c_cons = 0

    #Identidicar cantidades
    for cara in texto:
        #Validacion para que sea una letra
        if cara.isalpha():
            if cara in voc:
                c_voc += 1
            else:
                c_cons += 1

    return c_voc, c_cons

# Mensaje de bienvenida
print("Hola, Bienvenido\n")
import time
time.sleep(2)

cad=input("Ingresa una cadena de texto: ")

#Proceso
#Colocamos esto de esta manera, sustitullendo los valores de v y con por c_voc y c_cons
v, con = vocal_cons(cad)

#Resultados
print(f"\nLa cantidade de vocales del texto es: {v}")
print(f"La cantidad de constantes del texto es: {con}")

input("\nPresione ENTER para cerrar el programa ")