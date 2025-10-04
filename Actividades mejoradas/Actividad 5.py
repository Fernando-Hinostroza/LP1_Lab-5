def guardar_bytes(nombre_archivo="actividad1.bin"):
    try:
        datos = bytearray(10)
        for i in range(len(datos)):
            datos[i] = 10 + i

        with open(nombre_archivo, "wb") as fichero:
            fichero.write(datos)

        print(f"Archivo '{nombre_archivo}' creado con éxito.")

    except Exception as e:
        print("Error al manejar el archivo:", e)

if __name__ == "__main__":
    guardar_bytes()
