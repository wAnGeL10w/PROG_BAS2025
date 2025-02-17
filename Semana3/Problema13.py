# Función para convertir temperaturas
def temperatura(valor, t_inicial, t_resultante):
    # Celsius a otras escalas
    if t_inicial == 1:
        if t_resultante == 2:  # Celsius a Fahrenheit
            return (valor * 9/5) + 32
        elif t_resultante == 3:  # Celsius a Kelvin
            return valor + 273.15
    # Fahrenheit a otras escalas
    elif t_inicial == 2:
        if t_resultante == 1:  # Fahrenheit a Celsius
            return (valor - 32) * 5/9
        elif t_resultante == 3:  # Fahrenheit a Kelvin
            return (valor - 32) * 5/9 + 273.15
    # Kelvin a otras escalas
    elif t_inicial == 3:
        if t_resultante == 1:  # Kelvin a Celsius
            return valor - 273.15
        elif t_resultante == 2:  # Kelvin a Fahrenheit
            return (valor - 273.15) * 9/5 + 32
    return None  # Si no se elige una opción válida

# Mensaje de bienvenida
print("Hola, Bienvenido\n")
import time
time.sleep(2)

# Opciones de temperatura
escalas = {1: "Celsius", 2: "Fahrenheit", 3: "Kelvin"}

# Pedir datos al usuario
temp = float(input("Ingresa la temperatura: "))
t_in = int(input("Ingresa la temperatura inicial\n1.-Celsius\n2.-Fahrenheit\n3.-Kelvin\n"))
t_f = int(input("Ingresa la temperatura final\n1.-Celsius\n2.-Fahrenheit\n3.-Kelvin\n"))

# Validar que las escalas ingresadas sean correctas
if t_in in escalas and t_f in escalas:
    if t_in == t_f:
        print("La escala inicial y final son iguales, la temperatura no cambia.")
    else:
        resultado = temperatura(temp, t_in, t_f)
        print(f"La temperatura de {temp}° {escalas[t_in]} convertida a {escalas[t_f]} es: {resultado}° {escalas[t_f]}")
else:
    print("La escala NO está incluida en el programa. Vuelve a ejecutarlo.")

input("\nPresione ENTER para cerrar el programa ")
