import os

class CatalogoPeliculas:
    
    ruta_archivo = "peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            #a es el modo append
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__())
        except Exception as e:
            print("Ocurrio una excepcion al agregar: ", e)
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catalogo de Peliculas")
            print(archivo.read())
        except Exception as e:
            print("Ocurrio una excepcion al listar peliculas: ", e)
        finally:
            archivo.close()
            
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo eliminado: ", CatalogoPeliculas.ruta_archivo)
        except Exception as e:
            print("Ocurrio una excepcion al eliminar: ", e)
