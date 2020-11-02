class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    #metodo sobreescrito de la clase object
    def __add__ (self, otro):
        return self.__nombre + " " + otro.__nombre
        

p1 = Persona("Juan")
p2 = Persona ("Karla")

#Una nueva forma de trabajar al operador +
print(p1+p2)