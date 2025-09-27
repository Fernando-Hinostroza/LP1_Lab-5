import os
import string

def contar_letras(contenido):
    contador = {}
    for c in contenido:
        if c.isalpha():  # Solo letras
            c = c.lower()
            contador[c] = contador.get(c, 0) + 1
    return contador

def main():
    try:
        archivo_nombre = input("Ingrese el nombre del archivo con extensión .txt: ").strip()
        if not archivo_nombre:
            raise ValueError("Debe ingresar un nombre de archivo válido.")
        if not archivo_nombre.lower().endswith(".txt"):
            raise ValueError("El archivo debe tener extensión .txt.")
        if not os.path.exists(archivo_nombre):
            raise FileNotFoundError(f"El archivo '{archivo_nombre}' no existe.")
        if os.stat(archivo_nombre).st_size == 0:
            print(f"El archivo '{archivo_nombre}' está vacío.")
            return

        with open(archivo_nombre, "r", encoding="utf-8") as f:
            contenido = f.read()

        if not contenido.strip():
            print("El archivo no contiene letras válidas.")
            return

        frecuencias = contar_letras(contenido)

        print("\nHistograma de letras:")
        for letra in sorted(frecuencias.keys()):
            print(f"{letra} -> {frecuencias[letra]}")

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
