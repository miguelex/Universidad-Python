from persona import Persona
from conexion import Conexion
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
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR))
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[3], registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas
    
    @classmethod
    def insertar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellidos(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al insertar persona: {e}')
        finally:
            Conexion.cerrar()
    
    @classmethod
    def actualizar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellidos(), persona.get_email(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al actualizar persona: {e}')
        finally:
            Conexion.cerrar()
            
    @classmethod
    def eliminar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepcion al eliminar persona: {e}')
        finally:
            Conexion.cerrar()
        
if __name__ == '__main__':
    #Seleccioanr registros
    #personas = PersonaDao.seleccionar()
    #for persona in personas:
    #    logger.debug(persona)
    #    logger.info(persona.get_id_persona())
    
    #Insertar registro
    #persona = Persona (nombre ="Pedro", apellidos="Najera", email ="pnajera@gmail.com")
    #registros_insertados = PersonaDao.insertar(persona)
    #logger.debug(f'Registros insertados: {registros_insertados}')
    
    #Actualziar un registro existente
    #persona = Persona (2, 'Karla', 'Gomez', 'kgomez@mail.com')
    #personas_actualizadas = PersonaDao.actualizar(persona)
    #logger.debug(f'Personas actualizadas: {personas_actualizadas}') 
    
    #Eliminar persona
    persona =Persona(id_persona=12)
    persona_eliminada = PersonaDao.eliminar(persona)
    logger.debug(f'Personas eliminadas: {persona_eliminada}')