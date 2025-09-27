import os

def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


def pedir_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip().lower()
        if opcion in opciones_validas:
            return opcion
        print(f"Opción inválida. Debe ser una de {opciones_validas}.")


def generar_tabla(numero, limite, archivo="tabla_propuesto.txt"):
    try:
        modo = "w"
        if os.path.exists(archivo):
            opcion = pedir_opcion(
                f"El archivo '{archivo}' ya existe. ¿Desea sobrescribirlo (s) o añadir al final (a)? [s/a]: ",
                ["s", "a"]
            )
            modo = "w" if opcion == "s" else "a"

        with open(archivo, modo, encoding="utf-8") as f:
            encabezado = f"\nTabla de multiplicar del {numero} (hasta {limite})\n"
            f.write(encabezado)
            f.write("-" * len(encabezado) + "\n")
            for i in range(1, limite + 1):
                linea = f"{numero} x {i} = {numero * i}\n"
                f.write(linea)
                print(linea.strip())

        print(f"\nTabla de multiplicar del {numero} guardada en '{archivo}'.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")


if __name__ == "__main__":
    print("\n--- Generador de Tablas de Multiplicar ---")
    numero = pedir_entero("Ingrese un número entero (1-10): ", 1, 10)
    limite = pedir_entero("¿Hasta qué número desea generar la tabla (10-20)? ", 10, 20)
    generar_tabla(numero, limite)
