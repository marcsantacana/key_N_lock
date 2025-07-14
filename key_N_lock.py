import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.fernet import Fernet
import random
import string
import os

# ================= FUNCIONES =================

def cargar_clave(archivo_clave="clave.key"):
    if os.path.exists(archivo_clave):
        with open(archivo_clave, "rb") as archivo:
            return archivo.read()
    else:
        clave = Fernet.generate_key()
        with open(archivo_clave, "wb") as archivo:
            archivo.write(clave)
        return clave

def cifrar_contraseña(contraseña, clave):
    fernet = Fernet(clave)
    return fernet.encrypt(contraseña.encode()).decode()

def descifrar_contraseña(contraseña_cifrada, clave):
    fernet = Fernet(clave)
    return fernet.decrypt(contraseña_cifrada.encode()).decode()

def guardar_contraseña_cifrada(contraseñas, clave, archivo="contraseñas_cifradas.txt"):
    with open(archivo, "a") as f:
        for contraseña in contraseñas:
            contraseña_cifrada = cifrar_contraseña(contraseña, clave)
            f.write(contraseña_cifrada + "\n")
    messagebox.showinfo("Éxito", f"Contraseñas guardadas cifradas en {archivo}")

def generar_contraseña(longitud, mayus, minus, numeros, especiales, ambiguos):
    caracteres = ""
    if mayus: caracteres += string.ascii_uppercase
    if minus: caracteres += string.ascii_lowercase
    if numeros: caracteres += string.digits
    if especiales: caracteres += string.punctuation
    if ambiguos:
        caracteres = caracteres.translate(str.maketrans('', '', 'l1O0'))
    
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")
    
    while True:
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        if not any(contraseña[i:i+3] in "abcdefghijklmnopqrstuvwxyz0123456789" for i in range(len(contraseña) - 2)):
            return contraseña

def generar_y_mostrar():
    try:
        cantidad = int(entry_cantidad.get())
        longitud = int(entry_longitud.get())

        if not (8 <= longitud <= 64):
            raise ValueError("La longitud debe estar entre 8 y 64.")
        if cantidad < 1:
            raise ValueError("Cantidad mínima es 1.")

        contraseñas.clear()
        output_text.delete(1.0, tk.END)

        for _ in range(cantidad):
            pwd = generar_contraseña(
                longitud,
                var_mayus.get(),
                var_minus.get(),
                var_numeros.get(),
                var_especiales.get(),
                var_ambiguos.get()
            )
            contraseñas.append(pwd)
            output_text.insert(tk.END, pwd + "\n")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def guardar_contraseñas():
    if not contraseñas:
        messagebox.showwarning("Advertencia", "No hay contraseñas para guardar.")
        return
    clave = cargar_clave()
    guardar_contraseña_cifrada(contraseñas, clave)

# ================ GUI PRINCIPAL ================

clave = cargar_clave()
contraseñas = []

root = tk.Tk()
root.title("Generador y Cifrador de Contraseñas")
root.geometry("500x600")
root.resizable(False, False)

frame_config = tk.LabelFrame(root, text="Configuración", padx=10, pady=10)
frame_config.pack(padx=10, pady=10, fill="x")

tk.Label(frame_config, text="Cantidad:").grid(row=0, column=0, sticky="w")
entry_cantidad = tk.Entry(frame_config, width=10)
entry_cantidad.grid(row=0, column=1)
entry_cantidad.insert(0, "5")

tk.Label(frame_config, text="Longitud:").grid(row=1, column=0, sticky="w")
entry_longitud = tk.Entry(frame_config, width=10)
entry_longitud.grid(row=1, column=1)
entry_longitud.insert(0, "16")

var_mayus = tk.BooleanVar(value=True)
var_minus = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_especiales = tk.BooleanVar(value=False)
var_ambiguos = tk.BooleanVar(value=False)

tk.Checkbutton(frame_config, text="Mayúsculas", variable=var_mayus).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame_config, text="Minúsculas", variable=var_minus).grid(row=2, column=1, sticky="w")
tk.Checkbutton(frame_config, text="Números", variable=var_numeros).grid(row=3, column=0, sticky="w")
tk.Checkbutton(frame_config, text="Especiales", variable=var_especiales).grid(row=3, column=1, sticky="w")
tk.Checkbutton(frame_config, text="Evitar ambiguos", variable=var_ambiguos).grid(row=4, column=0, sticky="w")

tk.Button(root, text="Generar contraseñas", command=generar_y_mostrar, bg="#4CAF50", fg="white").pack(pady=10)

output_text = scrolledtext.ScrolledText(root, height=15, width=60)
output_text.pack(padx=10)

tk.Button(root, text="Guardar cifradas", command=guardar_contraseñas, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
