class TipoImagen:
    @staticmethod
    def chequearImagenBMP(archivo):
        try:
            with open(archivo, "rb") as archivo_binario:
                contenido = archivo_binario.read(2)
                # BMP inicia con los bytes "BM" -> 0x42, 0x4D
                return contenido[:2] == b"BM"
        except FileNotFoundError:
            print(f"Error: El archivo '{archivo}' no existe.")
        except Exception as e:
            print(f"Error al abrir el archivo '{archivo}': {e}")
        return False

print("Prueba 1 (BMP):", TipoImagen.chequearImagenBMP("imagen_bmp.bmp"))
print("Prueba 2 (JPG):", TipoImagen.chequearImagenBMP("imagen_jpg.jpg"))
print("Prueba 3 (PNG):", TipoImagen.chequearImagenBMP("imagen_png.png"))
