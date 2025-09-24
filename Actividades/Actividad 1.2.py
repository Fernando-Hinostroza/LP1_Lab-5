from io import open  
archi = open("archivo.txt","r")  
txt = archi.read()  
print(txt) 
archi.close() 