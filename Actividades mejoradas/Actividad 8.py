import pickle

def leer_lista(nombre_archivo="actividad3.pckl"):

    try:
        with open(nombre_archivo, "rb") as archivo:
            lista = pickle.load(archivo)
        print(f"Lista cargada desde '{nombre_archivo}': {lista}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print("Error al leer el archivo:", e)

if __name__ == "__main__":
    leer_lista()
