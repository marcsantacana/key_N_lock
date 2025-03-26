from cryptography.fernet import Fernet
import random
import string

# Generar o cargar una clave de cifrado
def cargar_clave(archivo_clave="clave.key"):
    try:
        with open(archivo_clave, "rb") as archivo:
            return archivo.read()
    except FileNotFoundError:
        clave = Fernet.generate_key()
        with open(archivo_clave, "wb") as archivo:
            archivo.write(clave)
        return clave

# Cifrar las contraseñas
def cifrar_contraseña(contraseña, clave):
    fernet = Fernet(clave)
    return fernet.encrypt(contraseña.encode()).decode()

# Descifrar las contraseñas
def descifrar_contraseña(contraseña_cifrada, clave):
    fernet = Fernet(clave)
    return fernet.decrypt(contraseña_cifrada.encode()).decode()

# Guardar contraseñas cifradas
def guardar_contraseña_cifrada(contraseñas, clave, archivo="contraseñas_cifradas.txt"):
    with open(archivo, "a") as f:
        for contraseña in contraseñas:
            contraseña_cifrada = cifrar_contraseña(contraseña, clave)
            f.write(contraseña_cifrada + "\n")
    print(f"Contraseñas cifradas guardadas en {archivo}")

# Generador de contraseñas (sin cambios)
def generar_contraseña(longitud=16, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_especiales=True, evitar_ambiguos=False):
    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation
    if evitar_ambiguos:
        caracteres = caracteres.translate(str.maketrans('', '', 'l1O0'))
    
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")
    
    while True:
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        if not any(contraseña[i:i+3] in "abcdefghijklmnopqrstuvwxyz0123456789" for i in range(len(contraseña) - 2)):
            break
    return contraseña

if __name__ == "__main__":
    try:
        clave = cargar_clave()
        cantidad = int(input("¿Cuántas contraseñas deseas generar?: "))
        if cantidad < 1:
            raise ValueError("La cantidad debe ser al menos 1.")
        
        longitud = int(input("Elige la longitud de la contraseña (8-64): "))
        if longitud < 8 or longitud > 64:
            raise ValueError("La longitud debe estar entre 8 y 64.")
        
        incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
        incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
        incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
        incluir_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
        evitar_ambiguos = input("¿Evitar caracteres ambiguos? (s/n): ").lower() == 's'
        
        contraseñas = []
        for _ in range(cantidad):
            contraseñas.append(generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales, evitar_ambiguos))
        
        print("\nContraseñas generadas:")
        for i, contraseña in enumerate(contraseñas, 1):
            print(f"{i}: {contraseña}")
        
        guardar = input("\n¿Quieres guardar estas contraseñas cifradas? (s/n): ").lower() == 's'
        if guardar:
            guardar_contraseña_cifrada(contraseñas, clave)
    except ValueError as e:
        print(f"Error: {e}")
