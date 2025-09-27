import os

class ErrorArchivo(Exception):
    """Excepcion para errores relacionados con el archivo"""

    def __init__(self, mensaje="Error en el manejo del archivo."):
        super().__init__(mensaje)

def es_jpg(ruta_archivo):
    """Verifica si un archivo es JPG leyendo sus primeros bytes"""
    try:
        if not os.path.exists(ruta_archivo):
            raise ErrorArchivo("El archivo no existe.")

        with open(ruta_archivo, "rb") as f:
            cabecera = f.read(2)
            return cabecera == b'\xff\xd8'

    except PermissionError:
        raise ErrorArchivo("No tiene permisos para leer el archivo.")
    except Exception as e:
        raise ErrorArchivo(f"Ocurrio un error inesperado: {e}")

def menu():
    print("\n--- Verificador de archivos JPG ---")
    ruta = input("Ingrese el nombre del archivo con extension: ").strip()

    try:
        if es_jpg(ruta):
            print(f"El archivo '{ruta}' es una imagen JPG valida.")
        else:
            print(f"El archivo '{ruta}' NO es una imagen JPG.")
    except ErrorArchivo as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    menu()
