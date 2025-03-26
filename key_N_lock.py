import random
import string

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
    
    # Evitar patrones predecibles
    while True:
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        if not any(contraseña[i:i+3] in "abcdefghijklmnopqrstuvwxyz0123456789" for i in range(len(contraseña) - 2)):
            break
    return contraseña

def guardar_contraseña(contraseñas, archivo="contraseñas.txt"):
    with open(archivo, "a") as f:
        for contraseña in contraseñas:
            f.write(contraseña + "\n")
    print(f"Contraseñas guardadas en {archivo}")

if __name__ == "__main__":
    try:
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
        
        guardar = input("\n¿Quieres guardar estas contraseñas? (s/n): ").lower() == 's'
        if guardar:
            guardar_contraseña(contraseñas)
    except ValueError as e:
        print(f"Error: {e}")
