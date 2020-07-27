#Set es una coleccion sin orden y tampoco tienen indices. No permite lementos repetidos
#Los elementos no se peudne modificar pero si agregar nuevos o eliminar

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

#largo
print(len(planetas))
#revisar si un elemento esta present
print("Marte" in planetas)
print("Tierra" in planetas)
#agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")
print(planetas)
#eliminar con remoce arroja excepcion si queremos borrar algo que no se enceuntre
planetas.remove("Tierra")
print(planetas)
#eliminar con discard
planetas.discard("Jupiter")
print(planetas)
#Limpiar el ser
planetas.clear()
print(planetas)
#eliminar el set
del planetas
print(planetas)
