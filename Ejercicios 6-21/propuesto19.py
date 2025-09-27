import pickle
import os

class Tarea:
    """Clase que representa una tarea"""
    def __init__(self, descripcion, fecha_vencimiento, estado="pendiente"):
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado

    def __str__(self):
        return f"{self.descripcion} | Vence: {self.fecha_vencimiento} | Estado: {self.estado}"

def mostrar_tareas(archivo="tareas.pkl"):
    if not os.path.exists(archivo):
        print("No se encontro el archivo de tareas.")
        return

    try:
        with open(archivo, "rb") as f:
            tareas = pickle.load(f)

        if not tareas:
            print("No hay tareas registradas.")
            return

        print("\n--- Lista de Tareas Guardadas ---")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

    except Exception as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    mostrar_tareas()
