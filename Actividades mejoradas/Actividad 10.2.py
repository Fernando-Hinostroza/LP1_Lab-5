import pickle

class Docente:
    def __init__(self, nombre, edad, horas):
        self.nombre = nombre
        self.edad = edad
        self.horas = horas
        print(f"Creación de nuevo docente: {self.nombre}")
    def __str__(self):
        return f"Nombre: {self.nombre} | Edad: {self.edad} | Horas: {self.horas}"

class ListaDocentes:
    def __init__(self):
        self.docentes = []
        try:
            with open("actividad6.bin", "rb") as archivo:
                self.docentes = pickle.load(archivo)
                print(f"Se cargaron {len(self.docentes)} docentes desde el archivo.")
        except (EOFError, FileNotFoundError):
            print("⚠️ El archivo está vacío o no existe, se creará uno nuevo.")
    def agregarDocente(self, docente):
        self.docentes.append(docente)
        self.guardarDocentesEnArchivo()
    def mostrarDocentes(self):
        if not self.docentes:
            print("No hay docentes registrados.")
        else:
            print("\nLista de docentes en memoria:")
            for d in self.docentes:
                print(d)
    def guardarDocentesEnArchivo(self):
        with open("actividad6.bin", "wb") as archivo:
            pickle.dump(self.docentes, archivo)
    def mostrarInformacionArchivo(self):
        print("\nInformación guardada en el archivo:")
        try:
            with open("actividad6.bin", "rb") as archivo:
                docentes = pickle.load(archivo)
                for d in docentes:
                    print(d)
        except Exception as e:
            print("Error al leer el archivo:", e)

miLista = ListaDocentes()

docente1 = Docente("Dely", 43, 30)
docente2 = Docente("Miguel", 24, 24)
docente3 = Docente("Leandro", 30, 18)

miLista.agregarDocente(docente1)
miLista.agregarDocente(docente2)
miLista.agregarDocente(docente3)

miLista.mostrarDocentes()
miLista.mostrarInformacionArchivo()
