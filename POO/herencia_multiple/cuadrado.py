from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def area(self):
        return self.alto * self.ancho
    
    def __str__ (self):
        return "Tenemos un cuadrado de medidas " + FiguraGeometrica.__str__(self) + " y de color = " + Color.get_color(self) + ". Su area es = " + str(Cuadrado.area(self))
