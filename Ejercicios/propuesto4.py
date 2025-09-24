def main():
    try:
        archivo_nombre = input("Ingrese el nombre del archivo a leer: ").strip()
        palabra_buscar = input("Ingrese la palabra que desea buscar: ").strip()
        
        if not archivo_nombre:
            raise ValueError("Debe ingresar un nombre de archivo válido.")
        if not palabra_buscar:
            raise ValueError("Debe ingresar una palabra para buscar.")
        
        with open(archivo_nombre, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        palabras = contenido.split()
        total_palabras = len(palabras)
        
        coincidencias = sum(1 for p in palabras if p.lower() == palabra_buscar.lower())
        
        print(f"El archivo tiene un total de {total_palabras} palabras.")
        print(f"La palabra '{palabra_buscar}' aparece {coincidencias} veces.")
    
    except FileNotFoundError:
        print("El archivo no existe en la carpeta actual.")
    except ValueError as ve:
        print("Error de validación:", ve)
    except IOError:
        print("Hubo un problema al leer el archivo.")
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
