import re
import tkinter as tk
from tkinter import messagebox

# Expresión regular para teléfono con código internacional
re_num = r'^\+\d{1,3}[-\s]?\d{6,12}$'

def validar_telefono():
    numero = entry_telefono.get()  # Obtener el texto de la entrada
    if re.match(re_num, numero):
        messagebox.showinfo("Resultado", "✅ El número de teléfono es válido.")
    else:
        messagebox.showerror("Resultado", "❌ El número de teléfono NO es válido.")

# Crear ventana
ventana = tk.Tk()
ventana.title("Validador de Teléfono Internacional")
ventana.geometry("350x150")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un número de teléfono (+CC Número):")
label.pack(pady=10)

# Caja de texto
entry_telefono = tk.Entry(ventana, width=30)
entry_telefono.pack()

# Botón de validación
boton_validar = tk.Button(ventana, text="Validar", command=validar_telefono)
boton_validar.pack(pady=10)

# Iniciar ventana
ventana.mainloop()
