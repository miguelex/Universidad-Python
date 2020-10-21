class Persona:
    def __init__(self, nombre, ape_paterno, ape_materno):
        self.nombre = nombre # Atributo publico
        self._apellido_paterno = ape_paterno # Atributo protegigo. Parcialmente privado. No necesita get ni set
        self.__apellido_materno = ape_materno # Atributo privado

    def metodo_publico(self):
        self.__metodo_privado()
                
    def __metodo_privado(self):
        # Metodo privado
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
        
p1 = Persona("Juan", "Lopez", "Mira")
p1.metodo_publico()

