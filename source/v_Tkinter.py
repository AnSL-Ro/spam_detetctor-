import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Has hecho clic en el botón!")

ventana = tk.Tk()
ventana.title("Ventana simple")

label = tk.Label(ventana, text="¡Hola, mundo!")
label.pack(pady=10)

boton = tk.Button(ventana, text="haz clic aqui", command=mostrar_mensaje)
boton.pack(pady=10)



ventana.mainloop()

