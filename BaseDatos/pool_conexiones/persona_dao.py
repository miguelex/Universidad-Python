from persona import Persona
from cursor_del_pool import CursorDelPool
from logger_base import logger

class PersonaDao:
    '''
       DAO (Data Access Object) 
       CRUD: Create-Read-Update-Delete entidad Persona
    '''
    
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellidos, email) VALUES (%s, %s, %s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre = %s, apellidos = %s, email = %s WHERE id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    
    @classmethod
    def seleccionar (cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[3], registro[3])
                personas.append(persona)
            return personas
        
    
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellidos(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
        
    
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellidos(), persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
                   
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount
        
        
if __name__ == '__main__':
    #Seleccioanr registros
    #personas = PersonaDao.seleccionar()
    #for persona in personas:
    #    logger.debug(persona)
    #    logger.info(persona.get_id_persona())
    
    #Insertar registro
    #persona = Persona (nombre ="Pedro2", apellidos="Najera2", email ="pnajera2@gmail.com")
    #registros_insertados = PersonaDao.insertar(persona)
    #logger.debug(f'Registros insertados: {registros_insertados}')
    
    #Actualziar un registro existente
    #persona = Persona (14, 'Karla', 'Gomez', 'kgomez@mail.com')
    #personas_actualizadas = PersonaDao.actualizar(persona)
    #logger.debug(f'Personas actualizadas: {personas_actualizadas}') 
    
    #Eliminar persona
    persona =Persona(id_persona=14)
    persona_eliminada = PersonaDao.eliminar(persona)
    logger.debug(f'Personas eliminadas: {persona_eliminada}')