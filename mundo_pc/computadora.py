from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computadora:
    
    contador_computadora = 0
    
    def __init__ (self, nombre, monitor, teclado , raton):
        Computadora.contador_computadora += 1
        self.__id_computadora = Computadora.contador_computadora
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
        
    def __str__(self):
        return (
            f"""
            {self.__nombre}: {self.__id_computadora}
                Monitor: {self.__monitor}
                Teclado: {self.__teclado}
                Raton: {self.__raton}
            """
        )
        
#monitor1 = Monitor("LG", "20")
#teclado1 = Teclado("Logictech", "Bluetooth")
#raton1 = Raton ("HP", "USB")
#computadora1 = Computadora("Hp", monitor1, teclado1, raton1)
#print(computadora1)