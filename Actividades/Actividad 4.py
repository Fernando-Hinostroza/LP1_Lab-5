# apertura el archivo y lo cierra al terminar de leer 
with open("archivobase.txt") as archi:    
    # recorrido del archivo línea a línea      
    for ln in archi:          
        # imprime línea leída          
        print(ln)  