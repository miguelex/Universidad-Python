from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
    print(tipo_padre)
    
empleado = Empleado ("Juan", 1000.00)
imprimir_detalles(empleado)

empleado = Gerente("Karla", 25000.00, "RRHH")
imprimir_detalles(empleado)