import customtkinter as ctk
import spam_detector
from tkinter import messagebox

def analizar_email():
    texto = entrada_email.get()

    if texto == "":
        messagebox.showinfo("Error", "Escribe un correo email antes de detectar")
        return
    resultado = spam_detector.predecir_spam(texto, modelo, vectorizer)

    if resultado == "SPAM":
        messagebox.showinfo("Aviso", "SPAM DETETCTADO")
        
    else:
        messagebox.showinfo("Aviso", "SPAM NO DETETCTADO")
        

def main():
    global modelo, vectorizer, entrada_email, etiqueta_resultado

    print("Entrenando modelo...")
    modelo, vectorizer = spam_detector.entrenar_modelo()

    accuary = spam_detector.evaluar_modelo(modelo, vectorizer)
    print(f"Precision del modelo: {accuary:.2f}")

    ventana = ctk.CTk()
    ventana.title("Detector de spam")
    ventana.geometry("500x300")

    titulo = ctk.CTkLabel(ventana, text="Detector de spam", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    instruccion = ctk.CTkLabel(ventana, text="Escribe un email para analizar")
    instruccion.pack()

    entrada_email = ctk.CTkEntry(ventana, width=400, placeholder_text="Escribe tu email aqui....")
    entrada_email.pack(pady=10)

    boton = ctk.CTkButton(ventana, text="Analizar", command=analizar_email, text_color="white", fg_color="#4CAF50", hover_color="#4D8150")
    boton.pack(pady=10)

    etiqueta_resultado = ctk.CTkLabel(ventana, text="", font=("Arial", 14))
    etiqueta_resultado.pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    main()

                          