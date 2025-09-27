import os

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def promedio(self):
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - Calificaciones: {self.calificaciones}"

ARCHIVO = "estudiantes.txt"

def guardar_estudiante(estudiante):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        calificaciones_str = ",".join(str(c) for c in estudiante.calificaciones)
        f.write(f"{estudiante.nombre};{estudiante.edad};{calificaciones_str}\n")

def cargar_estudiantes():
    estudiantes = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                try:
                    nombre, edad, calificaciones_str = linea.strip().split(";")
                    calificaciones = [float(c) for c in calificaciones_str.split(",") if c]
                    estudiantes.append(Estudiante(nombre, int(edad), calificaciones))
                except ValueError:
                    continue
    return estudiantes

def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        edad = int(input("Ingrese la edad del estudiante: ").strip())
        if edad <= 0:
            raise ValueError
    except ValueError:
        print("La edad debe ser un número entero positivo.")
        return

    try:
        calificaciones = input("Ingrese las calificaciones separadas por comas: ").strip()
        calificaciones = [float(c) for c in calificaciones.split(",") if c.strip()]
    except ValueError:
        print("Las calificaciones deben ser números válidos.")
        return

    estudiante = Estudiante(nombre, edad, calificaciones)
    guardar_estudiante(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")

def ver_estudiantes():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\nLISTA DE ESTUDIANTES")
    for est in estudiantes:
        print(est)

def promedio_estudiante():
    estudiantes = cargar_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    nombre = input("Ingrese el nombre del estudiante para calcular el promedio: ").strip()
    encontrados = [est for est in estudiantes if est.nombre.lower() == nombre.lower()]

    if encontrados:
        for est in encontrados:
            print(f"El promedio de {est.nombre} es: {est.promedio():.2f}")
    else:
        print("El estudiante no existe en los registros.")

def menu():
    while True:
        print("\nMENÚ ESTUDIANTES")
        print("1) Registrar estudiante")
        print("2) Ver lista de estudiantes")
        print("3) Obtener promedio de un estudiante")
        print("4) Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            ver_estudiantes()
        elif opcion == "3":
            promedio_estudiante()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)
