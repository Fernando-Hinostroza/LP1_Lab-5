import pickle
import os

class ErrorArchivo(Exception):
    def __init__(self, mensaje="Error en el manejo del archivo."):
        super().__init__(mensaje)

class ErrorFormatoFecha(Exception):
    def __init__(self, mensaje="Formato de fecha invalido. Use DD/MM/AAAA."):
        super().__init__(mensaje)

class Tarea:
    def __init__(self, descripcion, fecha_vencimiento, estado="pendiente"):
        self.descripcion = descripcion.strip()
        self.fecha_vencimiento = self._validar_fecha(fecha_vencimiento)
        self.estado = estado.lower()

    def _validar_fecha(self, fecha):
        import re
        patron = r"^\d{2}/\d{2}/\d{4}$"
        if not re.match(patron, fecha):
            raise ErrorFormatoFecha()
        return fecha

    def completar(self):
        self.estado = "finalizada"

    def __str__(self):
        return f"{self.descripcion} | Vence: {self.fecha_vencimiento} | Estado: {self.estado}"

class GestorTareas:
    def __init__(self, archivo="tareas.pkl"):
        self.archivo = archivo
        self.tareas = self._cargar()

    def _cargar(self):
        if not os.path.exists(self.archivo):
            return []
        try:
            with open(self.archivo, "rb") as f:
                return pickle.load(f)
        except Exception:
            return []

    def _guardar(self):
        """Guarda las tareas en un archivo pickle"""
        try:
            with open(self.archivo, "wb") as f:
                pickle.dump(self.tareas, f)
        except Exception:
            raise ErrorArchivo("No se pudo guardar el archivo de tareas.")

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        self._guardar()

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
            self._guardar()
        else:
            raise IndexError("El indice de la tarea no existe.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea}")

def menu():
    gestor = GestorTareas()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1) Agregar tarea")
        print("2) Completar tarea")
        print("3) Listar tareas")
        print("4) Salir")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                descripcion = input("Descripcion de la tarea: ")
                fecha = input("Fecha de vencimiento (DD/MM/AAAA): ")
                tarea = Tarea(descripcion, fecha)
                gestor.agregar_tarea(tarea)
                print("Tarea agregada con exito.")

            elif opcion == "2":
                gestor.listar_tareas()
                try:
                    indice = int(input("Ingrese el numero de la tarea a completar: ")) - 1
                    gestor.completar_tarea(indice)
                    print("Tarea completada con exito.")
                except ValueError:
                    print("Debe ingresar un numero valido.")
                except IndexError as e:
                    print(e)

            elif opcion == "3":
                gestor.listar_tareas()

            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida. Intente nuevamente.")

        except (ErrorFormatoFecha, ErrorArchivo) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    menu()
