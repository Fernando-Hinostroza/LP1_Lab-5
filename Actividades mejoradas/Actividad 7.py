import pickle

def guardar_lista(nombre_archivo="actividad3.pckl"):

    lista = [1, 2, 3, 4, 5]
    try:
        with open(nombre_archivo, "wb") as archivo:
            pickle.dump(lista, archivo)
        print(f"Lista guardada correctamente en '{nombre_archivo}'")
    except Exception as e:
        print("Error al guardar la lista:", e)

if __name__ == "__main__":
    guardar_lista()
