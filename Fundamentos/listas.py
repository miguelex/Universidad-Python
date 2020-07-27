nombres = ["Juan", "Karla", "Ricardo", "Maria"]

print(nombres)
#Conocer largo de la lista
print(len(nombres))
#elemento 0
print(nombres[0])
print(nombres[1])
#navegacion inverda
print(nombres[-1])
print(nombres[-2])
#imprimir rango
print(nombres[0:2]) #sin incluir el indice 2
#imprimir los elementos de inicio hasta el indice indicado
print(nombres[:3])
#imprimir los elelemtnos hasta el final desde el indice indicado
print(nombres[1:])
#cambiar los elementos de una lsita
nombres[3]  = "Ivone"
print(nombres)
#iterar la lista
for nombre in nombres:
    print(nombre)
    
#revisar si existe un elemento
if "Karla" in nombres:
    print("Karla si existe en la lsita")
else:
    print("El elemento indicado no existe en la lista")
    
#agregar nuevo elemento
nombres.append("Miguel")
print(nombres)
#insertar un nuevo elemento en el indice proporcioando
nombres.insert(1, "Lorenzo")
print(nombres)
#Quitar un elemento
nombres.remove("Lorenzo")
print(nombres)
#Quitar el ultimo elemento de la lsita
nombres.pop()
print(nombres)
#quitar el indice indicado de la lista
del (nombres[0])
print(nombres)
#limpiar elementos de neustra lsita
nombres.clear()
print(nombres)
#eliminar lista
del nombres
print(nombres)