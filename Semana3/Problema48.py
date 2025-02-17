#Esta libreria nos permite trabajar con situaciones, numeros o cosas aleatorias
import random

# Listas de nombres y apellidos
nomb=["Jose", "Hernán", "Pedro", "Angel", "Leonardo", "Fernanda", "Anna", "Maria", "Andrea", "Fátima"]
ap=["Sánchez", "Hernández", "Gonzales", "Pérez", "Martínez", "Morales", "Santiago", "Torres", "Villalobos", "Castillo"]

def nombre_c():
    #Se seleccionara un nombre y un apellido de manera aleatoria
    nombre=random.choice(nomb)
    apellido1=random.choice(ap)
    apellido2=random.choice(ap)
    #El valor que se va a regresar sera el nombre y el apellido
    return f"{nombre} {apellido1} {apellido2}"

#Bienvenida
print("Hola, Bienvenido\n")
import time
time.sleep(2)
cant= int(input("¿Cuántos nombres quieres generar?: "))

#Proceso
print("\nNombres generados:")
for i in range(cant):
    print(nombre_c())

input("\nPresiona ENTER para cerrar el programa ")