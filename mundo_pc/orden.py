class Orden():
    
    contador_ordenes = 0
    
    def __init__(self, computadoras):
        
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = computadoras
        
    def agregar_computadora (self, computadora):
        self.__computadoras.append(computadora)
        
    def __str__(self):
        computadora_str = ""
        for computadora in self.__computadoras:
            computadora_str +=computadora.__str__()
        
        return (
            f"Orden: {self.__id_orden}, "
            f"Computadoras: {computadora_str}, "
        )