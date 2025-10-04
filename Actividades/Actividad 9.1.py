#Programar si un archivo está en formato BMP 
class TipoImagen:     
    @staticmethod     
    def chequearImagenBMP(archivo):         
        archivo_binario=open(archivo,"rb")         
        contenido=archivo_binario.read(2)         
        if contenido[0]==0x42 and contenido[1]==0x4D:              
            return True         
        return False      
#Prueba de revision 
print("Prueba 1:",TipoImagen.chequearImagenBMP("imagen_bmp.bmp")) 
print("Prueba 2:",TipoImagen.chequearImagenBMP("imagen_jpg.jpg")) 
print("Prueba 3:",TipoImagen.chequearImagenBMP("imagen_png.png")) 