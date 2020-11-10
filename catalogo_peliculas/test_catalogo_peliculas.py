from Dominio.pelicula import Pelicula
from Servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None

while opcion != "4":
    print("Opciones")
    print("1. Agregar pelicula")
    print("2. Listar peliculas")
    print("3. Eliminar catalogo de peliculas")
    print("4. Salir")
    
    opcion = input(print("Escribe tu opcion (1-4)"))
    
    if opcion == "1":
        nombre_pelicula = input("Proporciona nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar()
else:
    print("Salimos del programa...")