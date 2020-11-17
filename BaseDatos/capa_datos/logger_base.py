import logging

# Variable logger a utilizar
logger = logging

logger.basicConfig(level = logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%d/%m/%Y %I:%M:%S %p',
                   handlers= [logging.FileHandler('capa_datos.log'),
                              logging.StreamHandler()
                              ]) # Solo para desarrollo o para descubrir un problema. En produccion ponerlo en INFO o WARNING

if __name__ == '__main__':
    logging.warning('mensaje nivel warning')
    logging.info('mensaje nivel info')
    logging.debug('mensaje nivel debug')
    logging.error('Ocurrio un error en la base de datos')
    logging.debug('Se realizo la conexión con éxito')