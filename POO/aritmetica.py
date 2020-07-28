class Aritmetica:
    """ Clase aritmetica para realziar las operaciones de simar, restar.... """
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def suma (self):
        return self.operando1 + self.operando2
    
#Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)
print("Resultado de la suma: ", aritmetica.suma())