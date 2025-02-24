#Para pbtener la susecion de fibonacci se utilizo la siguiente formula f(n) = f(n-1) + f(n-2)
from functools import lru_cache
@lru_cache(maxsize=None)
#Esta funcion hace que memorize los valores de la funcion para no tener que volver a calcularlos

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

import time
time.sleep(2)

n1=(int(input("Ingrese el numero de elementos de la serie de fibonacci: ")))
for i in range(n1):
    print(fibonacci(i))

input("Presione ENTER para salir")