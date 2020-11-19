from logging import log
from conexion import Conexion
from logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    #inicio de with
    def __enter__(self):
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        logger.debug(f'Inicio de with metodo __enter:: {self.__conn}')
        
    #fin del bloque with
    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug('Se ejecuta metodo __exit__() ')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'(Ocurrio una excepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug(f'Commit de la transaccion')
        # Cerramos el cursor
        self.__cursor.close()    
        #Regresar la conexioon al pool
        Conexion.liberarConexion(self.__conn)