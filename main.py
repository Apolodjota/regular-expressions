import tkinter as tk
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@unl\.edu$'
    return re.match(pattern, email) is not None

def verificar():
    correo = entry.get()
    if validate_email(correo):
        resultado_label.config(text="Correo válido", fg="green")
    else:
        resultado_label.config(text="Correo inválido - Solo se acepta dominio @unl.edu", fg="red")

root = tk.Tk()
root.title("Validador de correo de la Universidad Nacional de Loja")
root.geometry("550x100")

label = tk.Label(root, text="Ingrese su correo electrónico:")
label.pack(pady=5)

entry = tk.Entry(root, width=35)
entry.pack(pady=5)

ejemplo_label = tk.Label(root, text="Ejemplo: romero.figueroa@unl.edu")
ejemplo_label.pack(pady=5)


verificar_btn = tk.Button(root, text="Verificar", command=verificar)
verificar_btn.pack(pady=5)

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=5)

root.mainloop()