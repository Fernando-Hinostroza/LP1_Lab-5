import os
import string

VOWELS = "aeiouAEIOU"

def contar_vocales(texto):
    letras = [c for c in texto if c.isalpha()]
    total_letras = len(letras)
    total_vocales = sum(1 for c in letras if c in VOWELS)
    vocales_detalle = {v: texto.count(v) for v in "aeiouAEIOU"}
    porcentaje = (total_vocales / total_letras * 100) if total_letras > 0 else 0
    return total_vocales, vocales_detalle, porcentaje

def guardar_resultado(texto_original, total_vocales, vocales_detalle, porcentaje):
    try:
        with open("vocales.txt", "w", encoding="utf-8") as f:
            f.write(f"Texto ingresado:\n{texto_original}\n\n")
            f.write(f"Total de vocales encontradas: {total_vocales}\n")
            f.write("Detalle por vocal:\n")
            for v, c in vocales_detalle.items():
                f.write(f"  {v}: {c}\n")
            f.write(f"Porcentaje de vocales sobre letras: {porcentaje:.2f}%\n")
        print("Resultado guardado en 'vocales.txt'.")
    except IOError:
        print("Error al escribir el archivo 'vocales.txt'.")

def opcion_cadena():
    try:
        frase = input("Ingrese una oración: ").strip()
        if not frase:
            raise ValueError("No se ingresó ningún texto.")
        total_vocales, vocales_detalle, porcentaje = contar_vocales(frase)
        guardar_resultado(frase, total_vocales, vocales_detalle, porcentaje)
    except ValueError as ve:
        print("Error de validación:", ve)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

def opcion_archivo():
    try:
        nombre = input("Ingrese el nombre del archivo con extensión .txt: ").strip()
        if not nombre:
            raise ValueError("Debe ingresar un nombre de archivo válido.")
        if not nombre.lower().endswith(".txt"):
            raise ValueError("El archivo debe tener extensión .txt")
        if not os.path.exists(nombre):
            raise FileNotFoundError(f"El archivo '{nombre}' no existe.")
        if os.stat(nombre).st_size == 0:
            print(f"El archivo '{nombre}' está vacío.")
            return

        with open(nombre, "r", encoding="utf-8") as f:
            contenido = f.read()

        total_vocales, vocales_detalle, porcentaje = contar_vocales(contenido)
        print(f"\nArchivo: {nombre}")
        print(f"Total de vocales: {total_vocales}")
        print("Detalle por vocal:")
        for v, c in vocales_detalle.items():
            print(f"  {v}: {c}")
        print(f"Porcentaje de vocales sobre letras: {porcentaje:.2f}%")
    except ValueError as ve:
        print("Error de validación:", ve)
    except FileNotFoundError as fnf:
        print("Error:", fnf)
    except IOError:
        print(f"Error al leer el archivo '{nombre}'.")
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Leer cadena de caracteres")
        print("2. Leer archivo")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            opcion_cadena()
        elif opcion == "2":
            opcion_archivo()
        elif opcion == "3":
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
