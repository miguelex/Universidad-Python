#un diccionario esta compuesto de lalve, valor (key,value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}

print (diccionario)
#largo
print(len(diccionario))
#accediendo a un ele,ento
print(diccionario["IDE"])
#otra forma pero mismo resultado
print(diccionario.get("IDE"))
#modificando valores
diccionario["IDE"] = "Integrated development enviroment"
print (diccionario)
#iterar
for termino in diccionario:
    print(termino)
for termino in diccionario:
    print(diccionario[termino])
for valor in diccionario.values():
    print (valor)
#comprobando existencia de un elemento
print("IDE" in diccionario)
#agregar nuevo elemento
diccionario["PK"] = "Primary Key"
print (diccionario)
#remover elemento
diccionario.pop("DBMS")
print (diccionario)
#limpiar
diccionario.clear()
print (diccionario)
#eliminar diccioanrio
del diccionario
print (diccionario)
