class Caja:
    def __init__(self, alto, ancho, larog):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
    
    def volumen(self):
        return self.alto * self.ancho * self.largo
    
alto = int(input("Proporciona el tamaño de la alto: ")) 
ancho = int(input("Proporciona el tamaño de la ancho: ")) 
largo = int(input("Proporciona el tamaño de la largo: ")) 

caja = Caja (alto, ancho, largo)

print("El volumen de la caja indicada es: ", caja.volumen())