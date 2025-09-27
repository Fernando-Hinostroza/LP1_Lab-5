import os
import sys

ARCHIVO = "contador.txt"
LIMITE_SUPERIOR = 1_000_000
LIMITE_INFERIOR = -1_000_000

def leer_contador():
    if not os.path.exists(ARCHIVO) or os.stat(ARCHIVO).st_size == 0:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write("0")
        return 0
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            contenido = f.read().strip()
            contador = int(contenido)
            return contador
    except ValueError:
        print("El archivo contiene un valor no numérico. Se reiniciará a 0.")
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write("0")
        return 0
    except PermissionError:
        raise PermissionError("No se tienen permisos para leer el archivo.")

def guardar_contador(contador):
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.write(str(contador))
    except PermissionError:
        raise PermissionError("No se tienen permisos para escribir en el archivo.")

def main():
    try:
        contador = leer_contador()

        if len(sys.argv) > 2:
            print("Solo se permite un argumento: 'inc' o 'dec'.")
        elif len(sys.argv) == 2:
            arg = sys.argv[1].lower()
            if arg == "inc":
                contador += 1
                print("Contador incrementado en 1.")
            elif arg == "dec":
                contador -= 1
                print("Contador decrementado en 1.")
            else:
                print("Argumento no reconocido. Use 'inc', 'dec' o sin argumentos.")

        # Validar límites
        if contador > LIMITE_SUPERIOR:
            contador = LIMITE_SUPERIOR
            print(f"Contador ajustado al límite superior ({LIMITE_SUPERIOR}).")
        elif contador < LIMITE_INFERIOR:
            contador = LIMITE_INFERIOR
            print(f"Contador ajustado al límite inferior ({LIMITE_INFERIOR}).")

        print(f"Valor actual del contador: {contador}")
        guardar_contador(contador)

    except PermissionError as pe:
        print("Error de permisos:", pe)
    except IOError:
        print("Error al leer o escribir el archivo.")
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
