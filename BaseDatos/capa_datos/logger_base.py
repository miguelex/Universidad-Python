import logging

logger = logging

logger.basicConfig(level = logging.DEBUG) # Solo para desarrollo o para descubrir un problema. En produccion ponerlo en INFO o WARNING

logging.warning('mensaje nivel warning')
logging.info('menaje nivel info')
logging.debug('menaje nivel debug')
logging.error('Ocurrio un error en la base de datos')
logging.debug('Se realizo la conexión con éxito')