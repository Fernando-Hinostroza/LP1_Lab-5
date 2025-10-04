datos = bytearray(10) 
try:     
    fichero = open('actividad1.bin', 'rb')     
    fichero.readinto(datos)    
    fichero.close()     
    for a in datos:         
        print(hex(a), end=' ')
except Exception as excepcion:     
    print("Error al abrir el fichero", excepcion) 