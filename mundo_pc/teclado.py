from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contador_teclados = 0
    
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
        self._marca = marca
        self._tipo_entrada = tipo_entrada
        
    def __str__(self):
        return (
            f"Id: {self.__id_teclado}, "
            f"Marca: {self._marca}, "
            f"Tipo de entrada: {self._tipo_entrada}."
        )
        
teclado = Teclado ("Logictech", "USB")
print(teclado)