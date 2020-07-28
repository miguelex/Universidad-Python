class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
base = int(input("Proporciona el tamaño de la base: ")) 
altura = int(input("Proporciona el tamaño de la altura: ")) 

rectangulo = Rectangulo (base, altura)

print("El area del rectangulo indicado es: ", rectangulo.area())