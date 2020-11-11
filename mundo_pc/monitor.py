class Monitor:
    
    contador_monitores = 0
    
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = marca
        self.__tamanio = tamanio
        
    def __str__(self):
        return (
            f"Id: {self.__id_monitor}, "
            f"Marca: {self.__marca}, "
            f"Tamaño: {self.__tamanio}."
        )
        
#monitor = Monitor("LG", "20")
#print(monitor)