import os

class ErrorFormatoAnio(Exception):
    """Error personalizado para validar el año de lanzamiento"""
    def __init__(self, mensaje="El año de lanzamiento no es válido."):
        super().__init__(mensaje)

class Pelicula:
    def __init__(self, titulo, director, anio):
        self.titulo = titulo
        self.director = director
        self.anio = anio

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor.strip():
            raise ValueError("El título no puede estar vacío.")
        self._titulo = valor.strip()

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, valor):
        if not valor.strip():
            raise ValueError("El director no puede estar vacío.")
        self._director = valor.strip()

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        if not valor.isdigit() or not (1888 <= int(valor) <= 2100):
            raise ErrorFormatoAnio("El año debe ser un número entre 1888 y 2100.")
        self._anio = int(valor)

    def __str__(self):
        return f"{self.titulo} | {self.director} | {self.anio}"

class SistemaPeliculas:
    ARCHIVO = "peliculas.txt"

    def __init__(self):
        if not os.path.exists(self.ARCHIVO):
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                f.write("")

    def agregar_pelicula(self, pelicula):
        with open(self.ARCHIVO, "a", encoding="utf-8") as f:
            f.write(str(pelicula) + "\n")
        print("Película agregada con éxito.")

    def listar_peliculas(self):
        with open(self.ARCHIVO, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        if not lineas:
            print("No hay películas registradas.")
            return
        print("\nLista de películas:")
        for linea in lineas:
            print(linea.strip())

    def buscar_pelicula(self, criterio):
        with open(self.ARCHIVO, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        encontrados = [l.strip() for l in lineas if criterio.lower() in l.lower()]
        if encontrados:
            print("\nResultados de la búsqueda:")
            for peli in encontrados:
                print(peli)
        else:
            print("No se encontraron coincidencias.")

def menu():
    sistema = SistemaPeliculas()
    while True:
        print("\n---SISTEMA DE REGISTRO DE PELICULAS---")
        print("1) Agregar película")
        print("2) Listar películas")
        print("3) Buscar película")
        print("4) Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                titulo = input("Ingrese el título: ")
                director = input("Ingrese el director: ")
                anio = input("Ingrese el año de lanzamiento: ")
                pelicula = Pelicula(titulo, director, anio)
                sistema.agregar_pelicula(pelicula)
            elif opcion == "2":
                sistema.listar_peliculas()
            elif opcion == "3":
                criterio = input("Ingrese título o director a buscar: ")
                sistema.buscar_pelicula(criterio)
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()
