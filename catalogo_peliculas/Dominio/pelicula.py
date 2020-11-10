class Pelicula:
    def __init__ (self, nombre):
        self.__nombre = nombre
        
    def ___str__(self):
        return "Pelicula: " + self.__nombre
    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(nombre):
        self.__nombre = nombre