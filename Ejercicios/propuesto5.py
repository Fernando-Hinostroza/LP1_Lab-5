def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    return contador

def opcion_cadena():
    frase = input("Ingrese una oración: ")
    total_vocales = contar_vocales(frase)
    try:
        with open("vocales.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"Texto ingresado: {frase}\n")
            archivo.write(f"Cantidad de vocales encontradas: {total_vocales}\n")
        print("El resultado se guardó en vocales.txt")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

def opcion_archivo():
    nombre = input("Ingrese el nombre del archivo con su extensión (ejemplo: texto.txt): ")
    try:
        with open(nombre, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        total_vocales = contar_vocales(contenido)
        print(f"El archivo '{nombre}' contiene {total_vocales} vocales.")
    except FileNotFoundError:
        print("Error: El archivo no existe, verifique el nombre e intente de nuevo.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Leer cadena de caracteres")
        print("2. Leer archivo")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            opcion_cadena()
        elif opcion == "2":
            opcion_archivo()
        elif opcion == "3":
            print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
