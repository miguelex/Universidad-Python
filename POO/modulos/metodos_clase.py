class MiClase:
    
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Metodo estático")
        print(MiClase.variable_clase)
        #Desde un metodo estatico no podemos acceder a una variable de instancia
        #print(MiClase.variable_instancia)
        
    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: " + str(cls))
        print(cls.variable_clase)
        #Desde un metodo estatico no podemos acceder a una variable de instancia
        #print(cls.variable_instancia)
        
    def metodo_instancia(self):
        self.metodo_clase(),
        self.metodo_estatico()
        
MiClase.metodo_estatico()
MiClase.metodo_clase()

objeto1 = MiClase()
objeto1.metodo_instancia()