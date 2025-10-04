def leer_bytes(nombre_archivo="actividad1.bin"):
    try:
        datos = bytearray(10)
        with open(nombre_archivo, "rb") as fichero:
            bytes_leidos = fichero.readinto(datos)

        if bytes_leidos > 0:
            print(f"Se leyeron {bytes_leidos} bytes desde '{nombre_archivo}':")
            for i, valor in enumerate(datos):
                print(f"Byte {i}: {hex(valor)}")
        else:
            print("El archivo está vacío.")

    except Exception as e:
        print("Error al abrir o leer el archivo:", e)

if __name__ == "__main__":
    leer_bytes()
