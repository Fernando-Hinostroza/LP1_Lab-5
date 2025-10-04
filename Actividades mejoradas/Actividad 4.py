def leer_lineas(nombre_archivo="archivobase.txt"):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archi:
            print(f"Leyendo el archivo: {nombre_archivo}\n")
            contador = 0
            for i, ln in enumerate(archi, start=1):
                print(f"{i}: {ln.strip()}")
                contador += 1
        print(f"\nTotal de líneas leídas: {contador}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

nombre = input("Digite el nombre del archivo (ejemplo.txt): ")
leer_lineas(nombre)
