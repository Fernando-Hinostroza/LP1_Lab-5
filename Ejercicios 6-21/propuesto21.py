import pickle
import os

class Personaje:
    def __init__(self, nombre, vida, ofensiva, proteccion, alcance):
        if not all(isinstance(x, int) and x > 0 for x in [vida, ofensiva, proteccion, alcance]):
            raise ValueError("Todos los atributos deben ser enteros positivos.")
        self.nombre = nombre.strip().title()
        self.vida = vida
        self.ofensiva = ofensiva
        self.proteccion = proteccion
        self.alcance = alcance

    def mostrar(self):
        return (f"{self.nombre} | Vida: {self.vida} | Ofensiva: {self.ofensiva} | "
                f"Proteccion: {self.proteccion} | Alcance: {self.alcance}")

class Gestor:
    def __init__(self, archivo="personajes.pkl"):
        self.archivo = archivo
        self.personajes = {}
        self.cargar()

    def agregar(self, personaje):
        if personaje.nombre in self.personajes:
            print(f"El personaje '{personaje.nombre}' ya existe. No se agrega de nuevo.")
        else:
            self.personajes[personaje.nombre] = personaje
            print(f"Personaje '{personaje.nombre}' agregado.")
            self.guardar()

    def borrar(self, nombre):
        nombre = nombre.strip().title()
        if nombre in self.personajes:
            del self.personajes[nombre]
            print(f"Personaje '{nombre}' eliminado.")
            self.guardar()
        else:
            print(f"No existe un personaje con el nombre '{nombre}'.")

    def mostrar(self):
        if not self.personajes:
            print("No hay personajes en el gestor.")
        else:
            print("\n--- Lista de Personajes ---")
            for personaje in self.personajes.values():
                print(personaje.mostrar())

    def guardar(self):
        try:
            with open(self.archivo, "wb") as f:
                pickle.dump(self.personajes, f)
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "rb") as f:
                    self.personajes = pickle.load(f)
            except Exception as e:
                print(f"Error al cargar archivo: {e}")
                self.personajes = {}
        else:
            self.personajes = {}

def pedir_entero(mensaje):
    """Solicita un número entero positivo validado."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print("Debe ingresar un número entero positivo.")


def menu():
    print("\n--- Administrador de Personajes ---")
    print("1. Añadir personaje")
    print("2. Eliminar personaje")
    print("3. Mostrar personajes")
    print("4. Salir")
    return input("Seleccione una opción: ")

if __name__ == "__main__":
    gestor = Gestor()

    while True:
        opcion = menu()

        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del personaje: ").strip()
                vida = pedir_entero("Ingrese puntos de vida: ")
                ofensiva = pedir_entero("Ingrese puntos de ofensiva: ")
                proteccion = pedir_entero("Ingrese puntos de proteccion: ")
                alcance = pedir_entero("Ingrese puntos de alcance: ")
                nuevo = Personaje(nombre, vida, ofensiva, proteccion, alcance)
                gestor.agregar(nuevo)
            except Exception as e:
                print(f"Error al crear personaje: {e}")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del personaje a eliminar: ")
            gestor.borrar(nombre)

        elif opcion == "3":
            gestor.mostrar()

        elif opcion == "4":
            print("Saliendo del programa. Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")
