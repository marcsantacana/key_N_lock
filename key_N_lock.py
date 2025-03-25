import random
import string

def generar_contraseña(longitud=16, incluir_especiales=True):
    caracteres = string.ascii_letters + string.digits
    if incluir_especiales:
        caracteres += string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

if __name__ == "__main__":
    longitud = int(input("Elige la longitud de la contraseña (16 o 32): "))
    print(" ")
    incluir_especiales = input("Incluir caracteres especiales? (s/n): ").lower() == 's'
    print(" ")
    print("Contraseña generada:", generar_contraseña(longitud, incluir_especiales))
    print(" ")
