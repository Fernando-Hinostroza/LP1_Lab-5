def leer_numeros(nombre):     
    try:         
        archi = open(nombre,'r')         
        suma = 0         
        contador = 0         
        ln = archi.readline()         
        while(ln):             
            try:                 
                suma += int(ln)                 
                contador += 1                 
                ln = archi.readline()             
            except:                
                print('Error en linea no es un numero')                   
        print('El resultado de a suma: ',suma)         
        print('El resultado del promedio: ',suma/contador)        
        archi.close()     
    except FileNotFoundError:         
        print('No existe el archivo llamado ', nombre)      
    return      
nombre=input('Digite nombre del archivo completo (ejemplo.txt): ') 
leer_numeros(nombre)