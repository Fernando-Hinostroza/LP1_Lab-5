from io import open  
archi = open("archivo.txt","r")  
ln = archi.readlines()  
archi.close() 
print(ln[0])  