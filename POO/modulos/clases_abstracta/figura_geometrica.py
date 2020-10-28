# ABC = Abstract Base Class

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        self.alto= alto
        self.ancho = ancho
    
    @abstractmethod
    def area(self):
        pass 