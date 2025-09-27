import os

class ErrorArchivo(Exception):
    def __init__(self, mensaje="Error en el manejo del archivo."):
        super().__init__(mensaje)

def es_png(ruta_archivo):

    try:
        ruta_archivo = os.path.abspath(ruta_archivo)
        if not os.path.exists(ruta_archivo):
            raise ErrorArchivo("El archivo no existe.")

        with open(ruta_archivo, "rb") as f:
            cabecera = f.read(8)
            return cabecera == b'\x89PNG\r\n\x1a\n'

    except PermissionError:
        raise ErrorArchivo("No tiene permisos para leer el archivo.")
    except Exception as e:
        raise ErrorArchivo(f"Ocurrio un error inesperado: {e}")

def menu():
    print("\n--- Verificador de archivos PNG ---")
    ruta = input("Ingrese el nombre o ruta completa del archivo: ").strip()

    try:
        if es_png(ruta):
            print(f"El archivo '{ruta}' es una imagen PNG valida.")
        else:
            print(f"El archivo '{ruta}' NO es una imagen PNG.")
    except ErrorArchivo as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    menu()
