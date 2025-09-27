import os

ARCHIVO = "agenda.txt"

def cargar_agenda():
    agenda = {}
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                try:
                    nombre, celular = linea.strip().split(";")
                    agenda[nombre] = celular
                except ValueError:
                    continue
    return agenda

def guardar_agenda(agenda):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for nombre, celular in agenda.items():
            f.write(f"{nombre};{celular}\n")

def consultar_celular(agenda):
    nombre = input("Ingrese el nombre del cliente: ").strip()
    if nombre in agenda:
        print(f"El celular de {nombre} es {agenda[nombre]}")
    else:
        print("El cliente no existe en la agenda.")

def añadir_celular(agenda):
    nombre = input("Ingrese el nombre del cliente: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    celular = input("Ingrese el número de celular: ").strip()
    if not celular.isdigit():
        print("El número de celular debe contener solo dígitos.")
        return
    agenda[nombre] = celular
    guardar_agenda(agenda)
    print(f"Cliente {nombre} agregado/actualizado correctamente.")

def eliminar_celular(agenda):
    nombre = input("Ingrese el nombre del cliente que desea eliminar: ").strip()
    if nombre in agenda:
        del agenda[nombre]
        guardar_agenda(agenda)
        print(f"Cliente {nombre} eliminado correctamente.")
    else:
        print("El cliente no existe en la agenda.")

def crear_agenda():
    if os.path.exists(ARCHIVO):
        opcion = input("El archivo agenda.txt ya existe. ¿Desea reemplazarlo? (s/n): ").lower()
        if opcion != "s":
            print("Operación cancelada.")
            return
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.write("")
    print("Se ha creado un nuevo archivo agenda.txt.")

def menu():
    agenda = cargar_agenda()
    while True:
        print("\nMENÚ AGENDA TELEFÓNICA")
        print("1) Consultar un celular")
        print("2) Añadir un celular")
        print("3) Eliminar un celular")
        print("4) Crear la agenda")
        print("5) Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            consultar_celular(agenda)
        elif opcion == "2":
            añadir_celular(agenda)
        elif opcion == "3":
            eliminar_celular(agenda)
        elif opcion == "4":
            crear_agenda()
            agenda = {}
        elif opcion == "5":
            print("Saliendo de la agenda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print("Ha ocurrido un error inesperado:", e)
