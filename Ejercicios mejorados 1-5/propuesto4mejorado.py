import os
import string
import unicodedata

def limpiar_texto(texto):
    texto = ''.join(c for c in texto if c not in string.punctuation)
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto

def main():
    try:
        archivo_nombre = input("Ingrese el nombre del archivo a leer (con extensión .txt): ").strip()
        palabra_buscar = input("Ingrese la palabra que desea buscar: ").strip()
        
        if not archivo_nombre:
            raise ValueError("Debe ingresar un nombre de archivo válido.")
        if not archivo_nombre.lower().endswith('.txt'):
            raise ValueError("El archivo debe tener extensión .txt")
        if not palabra_buscar:
            raise ValueError("Debe ingresar una palabra para buscar.")
        if not palabra_buscar.isalpha():
            raise ValueError("La palabra a buscar solo debe contener letras.")

        if not os.path.exists(archivo_nombre):
            raise FileNotFoundError(f"El archivo '{archivo_nombre}' no existe en la carpeta actual.")

        with open(archivo_nombre, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        if not contenido.strip():
            print("El archivo está vacío.")
            return
        
        contenido_limpio = limpiar_texto(contenido).lower()
        palabras = contenido_limpio.split()
        total_palabras = len(palabras)
        
        palabra_limpia = limpiar_texto(palabra_buscar).lower()
        coincidencias = sum(1 for p in palabras if p == palabra_limpia)
        
        print(f"\nEl archivo '{archivo_nombre}' tiene un total de {total_palabras} palabras.")
        print(f"La palabra '{palabra_buscar}' aparece {coincidencias} veces.")
    
    except FileNotFoundError as fe:
        print("Error:", fe)
    except ValueError as ve:
        print("Error de validación:", ve)
    except IOError:
        print("Hubo un problema al leer el archivo.")
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    main()
