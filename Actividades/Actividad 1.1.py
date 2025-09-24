from io import open  
archi = open("archivo.txt","w")  
txt = "La vida es bella!!!" 
archi.write(txt)  
archi.close() 