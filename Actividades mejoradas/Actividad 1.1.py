import os

def crear_archivo():
    with open("archivo.txt", "w") as archi:
        texto = "La vida es bella!!!"
        archi.write(texto)
    print("Archivo creado y escrito correctamente.\n")

def leer_completo():
    if not os.path.exists("archivo.txt"):
        print("El archivo no existe. Primero créalo.\n")
        return
    with open("archivo.txt", "r") as archi:
        contenido = archi.read()
    print("Contenido completo del archivo:")
    print(contenido + "\n")

def leer_lineas_numeradas():
    if not os.path.exists("archivo.txt"):
        print("El archivo no existe. Primero créalo.\n")
        return
    with open("archivo.txt", "r") as archi:
        lineas = archi.readlines()
    print("Contenido línea por línea:")
    for i, linea in enumerate(lineas, start=1):
        print(f"{i}: {linea.strip()}")
    print()

def agregar_linea():
    if not os.path.exists("archivo.txt"):
        print("El archivo no existe. Primero créalo.\n")
        return
    nueva_linea = input("Ingresa la nueva línea a agregar: ")
    with open("archivo.txt", "a") as archi:
        archi.write("\n" + nueva_linea)
    print("➕ Nueva línea agregada al archivo.\n")

def menu():
    while True:
        print("====== MENÚ MANEJO DE ARCHIVOS ======")
        print("1. Crear archivo y escribir una línea")
        print("2. Leer todo el contenido")
        print("3. Leer archivo línea por línea numerada")
        print("4. Agregar línea al archivo")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            leer_completo()
        elif opcion == "3":
            leer_lineas_numeradas()
        elif opcion == "4":
            agregar_linea()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")

if __name__ == "__main__":
    menu()
