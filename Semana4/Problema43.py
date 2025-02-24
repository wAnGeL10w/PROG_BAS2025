import tkinter as tk
from tkinter import messagebox

#Declaramos una funcion para mostrar un mensaje
def Mensaje():
    texto = palabra.get()
    messagebox.showinfo("Mensaje", f"Has escrito: {texto}")

#Damos propiedades a la ventana
interfaz= tk.Tk()
#Este sera el titulo que tenga la ventana en la parte superior
interfaz.title("VENTANA DE INICIO")
#Dimensiones de la ventana
interfaz.geometry("400x250")

#Labels (cuadros de textos) que se verán en la pantalla
tk.Label(interfaz, text="Hola, Bienvenido").pack(pady=3)
tk.Label(interfaz, text="Escribe una palabra:").pack(pady=3)

#Entrada de texto en la interfaz
palabra=tk.Entry(interfaz)
palabra.pack(pady=5)

#Boton que al ser presionado mostrara un mensaje
boton=tk.Button(interfaz, text="Mostrar", command=Mensaje)
boton.pack(pady=5)

#PErmite que la ventana se mantenga abierta y no cierre
interfaz.mainloop()
