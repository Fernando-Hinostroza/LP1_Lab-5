datos = bytearray(10)  
for a in range(len(datos)):     
    datos[a] = 10 + a 
try:     
    fichero = open('actividad1.bin', 'wb')      
    fichero.write(datos)     
    fichero.close() 
except Exception as excepcion:     
    print("Error al abrir el fichero ",excepcion) 