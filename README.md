# key_N_lock

Este es un generador de contraseñas seguras desarrollado en **Python**. Permite generar contraseñas aleatorias según las preferencias del usuario.

## Características

-   Longitud configurable de la contraseña.
    
-   Opciones para incluir:
    
    -   Letras minúsculas y mayúsculas.
        
    -   Números.
        
    -   Caracteres especiales.
        
-   Copiar la contraseña generada al portapapeles.
    
-   **Cargar o generar clave de cifrado:** Se guarda en un archivo `clave.key` para reutilizarla.
    
-   **Cifrado y descifrado:** Se utiliza `cryptography.fernet` para cifrar y descifrar contraseñas.
    
-   **Guardar contraseñas cifradas:** Las contraseñas se guardan cifradas en un archivo `contraseñas_cifradas.txt`.
    

## Instalación

### Requisitos

-   **Python** (compilador compatible con C++17 o superior)

-   **cryptography** (si se usa cifrado en Python)

```
git clone https://github.com/marcsantacana/key_N_lock.git
cd key_N_lock
pip install cryptography
python key_N_lock.py
```

## Capturas de pantalla

- v1.0.0
<img width="510" height="252" alt="image" src="https://github.com/user-attachments/assets/b3f452bc-1f15-4e31-a167-5a928cfb8605" />

- v2.0.0
<img width="520" height="644" alt="image" src="https://github.com/user-attachments/assets/ebe36149-d94a-4f9a-83de-d4e18c6f86ae" />


## Licencia

Este proyecto está bajo la licencia **MIT**. Puedes usarlo, modificarlo y compartirlo libremente.


## Contacto

Si tienes dudas o sugerencias contactame por github o por linkedin.
