try:
    archivo = open("prueba.txt", "w")
    archivo.write("Agregamos info al archivo\n")
    archivo.write("adios")
except  Exception as e:
    print(e)
finally:
    archivo.close()
