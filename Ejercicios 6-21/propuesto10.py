class AgendaError(Exception):
    """Clase base para excepciones personalizadas."""
    pass
class ArchivoNoEncontradoError(AgendaError):
    """Se lanza cuando el archivo no existe."""
    pass
class ArchivoVacioError(AgendaError):
    """Se lanza cuando el archivo está vacío."""
    pass
class FormatoInvalidoError(AgendaError):
    """Se lanza cuando una línea no cumple el formato esperado."""
    pass

def leer_puntos(archivo_nombre):
    """Lee el archivo y acumula los puntos por alumno."""
    alumnos = {}

    try:
        with open(archivo_nombre, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        if not lineas:
            raise ArchivoVacioError("El archivo está vacío.")

        for linea in lineas:
            partes = linea.strip().split()
            if len(partes) < 3:
                raise FormatoInvalidoError(f"Línea mal formada: {linea.strip()}")
            
            nombre = partes[0]
            apellido = partes[1]
            try:
                puntos = float(partes[2])
            except ValueError:
                raise FormatoInvalidoError(f"Puntos inválidos en la línea: {linea.strip()}")
            
            clave = f"{nombre} {apellido}"
            alumnos[clave] = alumnos.get(clave, 0) + puntos

        return alumnos

    except FileNotFoundError:
        raise ArchivoNoEncontradoError("El archivo no existe en la carpeta actual.")
    except AgendaError:
        raise
    except Exception as e:
        raise AgendaError(f"Error inesperado: {e}")

def mostrar_reporte(alumnos):
    """Imprime el reporte ordenado alfabéticamente."""
    print("\nREPORTE DE PUNTOS\n")
    for alumno in sorted(alumnos.keys()):
        print(f"{alumno}: {alumnos[alumno]} puntos")

def main():
    try:
        archivo_nombre = input("Ingrese el nombre del archivo con su extensión: ").strip()
        if not archivo_nombre:
            raise ValueError("Debe ingresar un nombre de archivo válido.")

        alumnos = leer_puntos(archivo_nombre)
        mostrar_reporte(alumnos)
    except ArchivoNoEncontradoError as e:
        print("Error de Archivo", e)
    except ArchivoVacioError as e:
        print("Archivo vacio", e)
    except FormatoInvalidoError as e:
        print("Formato Invalido", e)
    except ValueError as e:
        print("Error de validación:", e)
    except AgendaError as e:
        print("Error en la agenda:", e)
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
