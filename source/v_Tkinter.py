
import customtkinter as ctk
from tkinter import messagebox

def main():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def mostrar_mensaje():
        
        messagebox.showinfo("Aviso", "Escaneo de spam completado")

    ventana = ctk.CTk()
    ventana.title("Spam detetctor")
    ventana.geometry("600x400")

    label = ctk.CTkLabel(ventana, text="Analizador de spam", font=("Arial", 20, "bold"))

    label.pack(pady=10)

    boton = ctk.CTkButton(ventana, text="Analizar Spam", fg_color= "green", command=mostrar_mensaje, hover_color="red")
    boton.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()