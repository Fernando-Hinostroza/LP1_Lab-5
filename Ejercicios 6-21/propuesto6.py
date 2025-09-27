import os
import string
import unicodedata

def limpiar_palabra(palabra):
    palabra = ''.join(c for c in palabra if c not in string.punctuation)
    palabra = unicodedata.normalize('NFKD', palabra).encode('ASCII', 'ignore').decode('utf-8')
    return palabra.lower()

def contar_palabras(contenido):
    palabras = contenido.split()
    contador = {}
    for palabra in palabras:
        palabra_limpia = limpiar_palabra(palabra)
        if palabra_limpia:  # Ignora cadenas vacías
            contador[palabra_limpia] = contador.get(palabra_limpia, 0) + 1
    return contador

def main():
    try:
        archivo_nombre = input("Ingrese el nombre del archivo con extensión .txt: ").strip()
        if not archivo_nombre:
            raise ValueError("Debe ingresar un nombre de archivo válido.")
        if not archivo_nombre.lower().endswith(".txt"):
            raise ValueError("El archivo debe tener extensión .txt")
        if not os.path.exists(archivo_nombre):
            raise FileNotFoundError(f"El archivo '{archivo_nombre}' no existe.")
        if os.stat(archivo_nombre).st_size == 0:
            print(f"El archivo '{archivo_nombre}' está vacío.")
            return

        with open(archivo_nombre, "r", encoding="utf-8") as f:
            contenido = f.read()

        if not contenido.strip():
            print("El archivo no contiene palabras válidas.")
            return

        diccionario_palabras = contar_palabras(contenido)

        print("\nConteo de palabras en el archivo:")
        for palabra, cantidad in diccionario_palabras.items():
            print(f"{palabra}: {cantidad}")

    except ValueError as ve:
        print("Error de validación:", ve)
    except FileNotFoundError as fnf:
        print("Error:", fnf)
    except IOError:
        print("Error al leer el archivo.")
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

if __name__ == "__main__":
    main()
