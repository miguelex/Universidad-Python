class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def __str__(self):
        return "Nombre: " + self.__nombre +", edad: " + str(self.__edad)
    