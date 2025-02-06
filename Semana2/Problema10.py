print("Hola, Bienvenido\n")
import time
time.sleep(2)

text=str(input("Escribe una cadena de texto: "))
print(f"Tu cadena fue: {text}\n")
v1=int(input("Desea realizar una modificacion?:\n1.Si      2.No\n"))
mod=v1%2
if v1==1 or v1==2:
    if v1==1:
        text=input(f"Texto original: {text}\nEscriba su nuevo texto:")
        print(f"Su cadena de texto nueva es: {text}\n")
    else:
        print(f"Su cadena de texto fue: {text}\n")
else:
    print("Opcion INVALIDA, vuelva a ejecitar el programa")
input("\nPresione ENTER para cerrar el programa ")