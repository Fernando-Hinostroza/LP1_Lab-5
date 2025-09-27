import pickle
import os

class Pelicula:
    def __init__(self, titulo, duracion, anio_lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.anio_lanzamiento = anio_lanzamiento

    def mostrar(self):
        return f"{self.titulo} | {self.duracion} min | Estreno: {self.anio_lanzamiento}"


class Catalogo:
    def __init__(self, archivo="peliculas.pkl"):
        self.archivo = archivo
        self.peliculas = []
        self.cargar()

    def agregar(self, pelicula):
        if isinstance(pelicula, Pelicula):
            self.peliculas.append(pelicula)
            print(f"Película '{pelicula.titulo}' agregada al catálogo.")
        else:
            print("Error: Solo se pueden agregar objetos de tipo Pelicula.")

    def mostrar(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            print("\n--- Catálogo de Películas ---")
            for i, pelicula in enumerate(self.peliculas, start=1):
                print(f"{i}. {pelicula.mostrar()}")

    def guardar(self):
        try:
            with open(self.archivo, "wb") as f:
                pickle.dump(self.peliculas, f)
            print("Catálogo guardado correctamente.")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def cargar(self):
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, "rb") as f:
                self.peliculas = pickle.load(f)
            print("Catálogo cargado correctamente.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

def menu():
    catalogo = Catalogo()

    while True:
        print("\n--- Menú Catálogo de Películas ---")
        print("1. Agregar película")
        print("2. Mostrar catálogo")
        print("3. Guardar catálogo")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la película: ").strip()
            try:
                duracion = int(input("Ingrese la duración en minutos: "))
                anio = int(input("Ingrese el año de lanzamiento: "))
                nueva = Pelicula(titulo, duracion, anio)
                catalogo.agregar(nueva)
            except ValueError:
                print("Error: La duración y el año deben ser números enteros.")

        elif opcion == "2":
            catalogo.mostrar()

        elif opcion == "3":
            catalogo.guardar()

        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
