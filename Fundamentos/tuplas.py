#Una tupla mantiene el orden oeri no se puede modificar

frutas = ("Naranja", "Platano", "Guayaba")

print(frutas)

#largo de la tupl
print(len(frutas))
#accediendo a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#rango
print(frutas[0:2]) #Excluyebdo indice 2
#modificar tupla
frutasLista = list(frutas)
frutasLista[1] = "Banana"
frutas = tuple(frutasLista)
print(frutas)
#iterar una tupla
for fruta in frutas:
    print(fruta, end =" ")
    
# no podemso agregar ni eliminear elementos de uan tupla
del frutas
print(frutas)