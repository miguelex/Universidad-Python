from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
       DAO (Data Access Object) 
       CRUD: Create-Read-Update-Delete entidad Persona
    '''
    
    __SELECCIONAR = ' SELECT * FROM persona ORDER BY id_persona'
    
    @classmethod
    def seleccionar (cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[3], registro[3])
            personas.append(persona)
        return personas
    
if __name__ == '__main__':
    personas = PersonaDao.seleccionar()
    for persona in personas:
        logger.debug(persona)
        logger.info(persona.get_id_persona())
    