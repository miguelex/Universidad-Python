archivo = open("prueba.txt", "r")
#print(archivo.read())

#Leer algunos caracteres
#print(archivo.read(5)) #Si no comento el print anterior no se me mostrara nada porque ya leyo el archivo
#print(archivo.read(3))

#Leer lienas completas. Tengo que comenbtar lo anterior

#print(archivo.readline())
#print(archivo.readline())

#for linea in archivo:
 #   print(linea)

#print(archivo.readlines())

#print(archivo.readlines()[1])

archivo2 = open("copia.txt", "w")
archivo2.write(archivo.read())

archivo2.close()
archivo.close()