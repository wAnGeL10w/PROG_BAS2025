import time
import os
saldo=0
ret_acum=0

#Funcion para evitar redundancia de codigo
def BorrarPantalla():
    time.sleep(2)
    os.system('cls')
    
#Funcion para Realizar operaciones bancarias
def CuentaBancaria():
    global saldo, ret_acum
    print("Hola, Bienvenido\n")
    while True:
        print("Menu de opciones")
        print("1. Depositar\n2. Retirar\n3. Consultar Saldo\n4. Salir")
        #strip() elimina los espacios en blanco al principio y al final de la cadena
        op=input("\nSeleccione una opción: ").strip()
        if op=="1":
            dep=float(input("Ingrese la cantidad a depositar: "))
            if dep<0:
                print("No se puede depositar cantidades negativas.")
                BorrarPantalla()
            else:
                #Acumulamos los depositos
                saldo+=dep
                print("Deposito realizado.")
                BorrarPantalla()
        elif op=="2":
            ret=float(input("\nIngrese la cantidad a retirar: "))
            if ret<0:
                print("No se puede retirar cantidades negativas.")
                BorrarPantalla()
            else:
                if ret>saldo:
                    print("Saldo insuficiente")
                    BorrarPantalla()
                else:
                    #El limite de retiros es de 10000
                    if ret_acum+ret>10000:
                        print("Ha alcanzado el limite de retiros.")
                        BorrarPantalla()
                    else:
                        saldo-=ret
                        #Acumulamos los retiros
                        ret_acum+=ret
                        print("Retiro realizado exitosamente.")
                        BorrarPantalla()
        elif op=="3":
            #Permite añadir 2 decimales al saldo
            print(f"Saldo: ${saldo:.2f}")
            BorrarPantalla()
        elif op=="4":
            break
        
#LLamamos a la función
CuentaBancaria()

input("Presione ENTER para cerrar el programa ")
