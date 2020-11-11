from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

teclado_hp = Teclado ("HP", "USB")
raton_hp = Raton ("HP", "USB")
monitor_hp = Monitor ("HP", "20 pulgadas")

computadora_hp = Computadora("HP", monitor_hp, teclado_hp, raton_hp)

teclado_ACER = Teclado ("ACER", "USB")
raton_ACER = Raton ("ACER", "USB")
monitor_ACER = Monitor ("ACER", "16 pulgadas")

computadora_ACER = Computadora("ACER", monitor_ACER, teclado_ACER, raton_ACER)

teclado_gamer = Teclado ("gamer", "Bluetooth")
raton_gamer = Raton ("gamer", "Bluetooth")
monitor_gamer = Monitor ("gamer", "45 pulgadas")

computadora_gamer = Computadora("GAMER", monitor_gamer, teclado_gamer, raton_gamer)

computadora_armada = Computadora("Armada", monitor_hp, teclado_gamer, raton_ACER)

computadoras1 = [computadora_ACER, computadora_hp]

orden1 = Orden (computadoras1)
print (orden1)

orden1.agregar_computadora(computadora_gamer)
print(orden1)

computadoras2 = [computadora_gamer, computadora_armada, computadora_ACER]
orden2 = Orden (computadoras2)
print(orden2)