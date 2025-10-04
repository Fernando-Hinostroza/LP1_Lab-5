import pickle

class Vehiculo:     
    def __init__(self, firma, version):         
        self.firma = firma         
        self.version = version         
        self.en_marcha = False        
        self.acelerando = False         
        self.frenando = False          
    def arrancar(self):         
        self.en_marcha = True      
    def acelerar(self):         
        self.acelerando = True      
    def frenar(self):         
        self.frenando = True          
    def estado(self):
        estado_str = (
            "Marca: " + self.firma +
            "\nModelo: " + self.version +
            "\nEn marcha: " + str(self.en_marcha) +
            "\nAcelerando: " + str(self.acelerando) +
            "\nFrenando: " + str(self.frenando) +
            "\n----------------------------------"
        )
        return estado_str
auto1 = Vehiculo("Honda", "CRV") 
auto2 = Vehiculo("Toyota", "Yaris") 
auto3 = Vehiculo("Nissan", "Sentra")  
autos = [auto1, auto2, auto3]  
with open("actividad5.pckl", "wb") as archivo_binario:
    pickle.dump(autos, archivo_binario)
with open("actividad5.pckl", "rb") as archivo_apertura:
    vehiculos = pickle.load(archivo_apertura)
for item in vehiculos:     
    print(item.estado())
del(archivo_apertura)