def crearArchivo(texto):     
    archi = open('prueba.txt','w',encoding='utf-8')     
    archi.write('Lenguaje de Programación I\n')     
    archi.write(texto)     
    archi.close()  
texto=input('Ingrese un texto a agregar al archivo: ') 
crearArchivo(texto) 