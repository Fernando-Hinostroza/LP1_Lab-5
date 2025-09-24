import os
import sys

def main():
    archivo = "contador.txt"
    contador = 0

    try:
        if not os.path.exists(archivo) or os.stat(archivo).st_size == 0:
            with open(archivo, "w", encoding="utf-8") as f:
                f.write("0")
        else:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                if contenido.isdigit() or (contenido.startswith("-") and contenido[1:].isdigit()):
                    contador = int(contenido)
                else:
                    raise ValueError("El archivo contiene un valor no numérico.")
        
        if len(sys.argv) > 1:
            argumento = sys.argv[1].lower()
            if argumento == "inc":
                contador += 1
            elif argumento == "dec":
                contador -= 1
            else:
                print("Argumento no reconocido. Use 'inc', 'dec' o sin argumentos.")
        
        print(f"Valor actual del contador: {contador}")
        
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(str(contador))

    except ValueError as ve:
        print("Error en los datos:", ve)
    except IOError:
        print("Error al leer o escribir el archivo.")
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
