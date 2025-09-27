import os
from datetime import datetime

class Tarea:
    def __init__(self, descripcion: str, fecha_vencimiento: str, estado: str = "Pendiente"):
        self.descripcion = descripcion.strip()
        self._fecha_vencimiento = None
        self.set_fecha_vencimiento(fecha_vencimiento)
        self.estado = estado if estado in ["Pendiente", "Completada"] else "Pendiente"

    def get_fecha_vencimiento(self):
        return self._fecha_vencimiento

    def set_fecha_vencimiento(self, fecha_str: str):
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            self._fecha_vencimiento = fecha
        except ValueError:
            raise ValueError("La fecha debe tener el formato DD/MM/AAAA")

    fecha_vencimiento = property(get_fecha_vencimiento, set_fecha_vencimiento)

    def marcar_completada(self):
        self.estado = "Completada"

    def __str__(self):
        return f"{self.descripcion} | {self.fecha_vencimiento.strftime('%d/%m/%Y')} | {self.estado}"
    
class GestorTareas:
    ARCHIVO = "tareas.txt"

    def __init__(self):
        self.tareas = []
        self.cargar_tareas()

    def cargar_tareas(self):
        if os.path.exists(self.ARCHIVO):
            try:
                with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                    for linea in f:
                        datos = linea.strip().split(" | ")
                        if len(datos) == 3:
                            descripcion, fecha_str, estado = datos
                            try:
                                tarea = Tarea(descripcion, fecha_str, estado)
                                self.tareas.append(tarea)
                            except ValueError:
                                print(f"[Aviso] Se omitio una tarea por fecha invalida: {linea.strip()}")
            except Exception as e:
                print(f"[Error] No se pudo leer el archivo: {e}")

    def guardar_tareas(self):
        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                for tarea in self.tareas:
                    f.write(str(tarea) + "\n")
        except Exception as e:
            print(f"[Error] No se pudo guardar el archivo: {e}")

    def agregar_tarea(self, descripcion, fecha_str):
        try:
            nueva_tarea = Tarea(descripcion, fecha_str)
            self.tareas.append(nueva_tarea)
            self.guardar_tareas()
            print("Tarea agregada correctamente.")
        except ValueError as e:
            print(f"[Error] {e}")

    def marcar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion.lower() == descripcion.lower() and tarea.estado == "Pendiente":
                tarea.marcar_completada()
                self.guardar_tareas()
                print("Tarea marcada como completada.")
                return
        print("No se encontro una tarea pendiente con esa descripcion.")

    def listar_pendientes(self):
        pendientes = [t for t in self.tareas if t.estado == "Pendiente"]
        if pendientes:
            print("\nTareas pendientes:")
            for i, tarea in enumerate(pendientes, 1):
                print(f"{i}. {tarea}")
        else:
            print("No hay tareas pendientes.")

def menu():
    gestor = GestorTareas()
    while True:
        print("\n--- Menu de Gestion de Tareas ---")
        print("1) Agregar tarea")
        print("2) Marcar tarea como completada")
        print("3) Listar tareas pendientes")
        print("4) Salir")

        opcion = input("Elige una opcion: ")
        if opcion == "1":
            desc = input("Descripcion de la tarea: ").strip()
            fecha = input("Fecha de vencimiento (DD/MM/AAAA): ").strip()
            gestor.agregar_tarea(desc, fecha)
        elif opcion == "2":
            desc = input("Descripcion de la tarea a completar: ").strip()
            gestor.marcar_completada(desc)
        elif opcion == "3":
            gestor.listar_pendientes()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

if __name__ == "__main__":
    menu()
