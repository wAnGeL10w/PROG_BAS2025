#Imoortamos la librería math para trabajar de mejor manera
import math

# Mensaje de bienvenida
print("Hola, Bienvenido\n")

def areas(v1):
    if v1 == 1: #Calculo de Area de cuadrado
        lado = float(input("Ingresa el lado del cuadrado: "))
        return lado ** 2
    elif v1 == 2: #Calculo de Area de rectangulo
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        return base * altura
    
    elif v1 == 3: #Calculo de Area de circulo
        radio = float(input("Ingresa el radio del círculo: "))
        return math.pi * (radio ** 2)
    
    elif v1 == 4: #Calculo de Area de triangulo
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        return (base * altura) / 2
    
    else:
        #Esta opcion es por si no se selecciona una opcion valida
        print("Opción no válida.")
        return None

def volumenes(v1):
    if v1 == 1: #Volumen de un cubo
        lado = float(input("Ingresa el lado del cubo: "))
        return lado ** 3
    
    elif v1 == 2: #Volumen de un prisma rectangular
        largo = float(input("Ingresa el largo del prisma: "))
        ancho = float(input("Ingresa el ancho del prisma: "))
        altura = float(input("Ingresa la altura del prisma: "))
        return largo * ancho * altura
    
    elif v1 == 3: #volumen de una esfera
        radio = float(input("Ingresa el radio de la esfera: "))
        return (4/3) * math.pi * (radio ** 3)
    
    elif v1 == 4: #Volumen de un cilindro
        radio = float(input("Ingresa el radio de la base del cilindro: "))
        altura = float(input("Ingresa la altura del cilindro: "))
        return math.pi * (radio ** 2) * altura
    
    else:
        #Esta opcion es por si no se selecciona una opcion valida
        print("Opción no válida.")
        return None

# Mensaje de bienvenida
print("Hola, Bienvenido\n")
import time
time.sleep(2)

# Menú principal
print("Selecciona una opción:")
print("1. Calcular área")
print("2. Calcular volumen")

opera = int(input("Selecciona una opción: "))

if opera == 1:
    print("\nSelecciona la figura geométrica para calcular el área:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
    
    opc=int(input("Selecciona una opción: "))
    resu=areas(opc)
    if resu is not None:
        print(f"El área es: {resu}")
    
elif opera == 2:
    print("\nSelecciona la figura geométrica para calcular el volumen:")
    print("1. Cubo")
    print("2. Prisma rectangular")
    print("3. Esfera")
    print("4. Cilindro")
    
    opc = int(input("Selecciona una opcion: "))
    resu=volumenes(opc)
    if resu is not None:
        print(f"El volumen es: {resu}")
else:
    print("Opción no válida.")

input("\nPresione ENTER para cerrar el programa ")
