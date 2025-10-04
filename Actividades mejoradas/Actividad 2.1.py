import os

def mostrar_info(nombre_archivo="archivo.txt"):
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.\n")
        return
    
    with open(nombre_archivo, "r", encoding="utf-8") as archi:
        print("Información del archivo:")
        print("Nombre:", archi.name)
        print("¿Está cerrado?:", archi.closed)
        print("Modo de apertura:", archi.mode)
    print("¿Está cerrado?:", archi.closed, "\n")

def crear_archivo(nombre_archivo="archivo.txt"):
    texto = input("Ingresa un texto para guardar en el archivo: ")
    with open(nombre_archivo, "w", encoding="utf-8") as archi:
        archi.write(texto)
    print(f"Archivo '{nombre_archivo}' creado con el texto ingresado.\n")

def agregar_texto(nombre_archivo="archivo.txt"):
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.\n")
        return
    texto = input("Ingresa un texto para agregar al archivo: ")
    with open(nombre_archivo, "a", encoding="utf-8") as archi:
        archi.write("\n" + texto)
    print("Texto agregado correctamente.\n")

def leer_archivo(nombre_archivo="archivo.txt"):
    if not os.path.exists(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' no existe.\n")
        return
    with open(nombre_archivo, "r", encoding="utf-8") as archi:
        contenido = archi.read()
    print("Contenido del archivo:")
    print(contenido + "\n")

def menu():
    while True:
        print("====== MENÚ ARCHIVOS ======")
        print("1. Crear archivo con texto")
        print("2. Mostrar información del archivo")
        print("3. Agregar texto al archivo")
        print("4. Leer contenido del archivo")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            mostrar_info()
        elif opcion == "3":
            agregar_texto()
        elif opcion == "4":
            leer_archivo()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")

if __name__ == "__main__":
    menu()
