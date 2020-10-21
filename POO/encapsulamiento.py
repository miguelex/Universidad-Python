class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre # Variable privada
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

p1 =Persona("Juan")
print(p1.get_nombre())  
p1.set_nombre("Karla")   
print(p1.get_nombre())    
