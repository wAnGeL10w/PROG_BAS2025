
#Usamos una función para mostrar el menú de la agenda
def MenuAgenda():
    print("\n MENÚ DE AGENDA ")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Salir")

#Funcion para agregar un contacto
#strip() elimina los espacios en blanco al principio y al final de la cadena
def AddCont(contactos):
    nom=input("Nombre: ").strip()
    tel=input("Teléfono: ").strip()
    #Guardamos el telefono en nueva variable
    contactos[nom] = tel
    print("Contacto agregado.")

#Funcion para buscar un contacto
#strip() elimina los espacios en blanco al principio y al final de la cadena
def BuscCont(contactos):
    nom=input("Nombre del contacto: ").strip()
    if nom in contactos:
        #Imprime el NOMBRE y el TELEFONO del contacto
        print(f" {nom}: {contactos[nom]}")
    else:
        print("Contacto no existente")

#Funcion para mostrar todos los contactos
def TotCont(contactos):
    #En caso de NO encontrar contactos imprime texto
    if not contactos:
        print("No hay contactos guardados.")
    else:
        #Si lo encuentra lo busca y lo imprime
        print("\n Agenda de Contactos ")
        #Itmes permite obtener los elementos de, en este caso los contactos
        for nom, tel in contactos.items():
            print(f" {nom}: {tel}")

#Funcion para eliminar un contacto
#strip() elimina los espacios en blanco al principio y al final de la cadena
def DelCont(contactos):
    nom=input("Nombre del contacto a eliminar: ").strip()
    if nom in contactos:
        del contactos[nom]
        print("Contacto eliminado.")
    else:
        print("Contacto no encontrado.")

#Funcion para ejecutar la agenda//Codigo Principal
def Agenda():
    cont = {}
    while True:
        import time
        time.sleep(2)
        MenuAgenda()
        op=input("Seleccione una opción: ").strip()
        if op =="1":
            AddCont(cont)
        elif op=="2":
            BuscCont(cont)
        elif op=="3":
            TotCont(cont)
        elif op=="4":
            DelCont(cont)
        elif op=="5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la agenda
Agenda()

input("Presione ENTER para cerrar el programa ")