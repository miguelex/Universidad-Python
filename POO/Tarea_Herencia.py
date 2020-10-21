class Vehiculo:
    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__ (self):
        return "Color Vehiculo: " + self.color + ", Nº Ruedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__ (self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
        
    def __str__ (self):
        return super().__str__()  + ", Velocidad: " + str(self.velocidad)
    
class Bicicleta(Vehiculo):
    def __init__ (self, color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo
        
    def __str__ (self):
        return super().__str__()  + ", Tipo: " + self.tipo

vehiculo = Vehiculo ("Rojo", 4)
print(vehiculo)

coche = Coche ("Blanco", 4, 210)
print(coche)

bicicleta = Bicicleta ("Azul", 2, "Montaña")
print(bicicleta)