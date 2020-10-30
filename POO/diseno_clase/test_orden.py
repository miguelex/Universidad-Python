from producto import Producto
from orden import Orden

producto1 = Producto("Camisa" , 100.00)
producto2 = Producto("Pantalon", 59.53)
producto3 = Producto("Calcetines", 25.36)

productos = [producto1, producto2]

orden1 = Orden(productos)
print(orden1)

productos.append(producto3)

orden1.agregar_producto(producto3)
print(orden1)
print(orden1.calcular_total())