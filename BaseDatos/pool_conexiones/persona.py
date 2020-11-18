from logger_base import logger


class Persona:
    def __init__(self, id_persona=None, nombre=None, apellidos=None, email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email

    def __str__(self):
        return (
            f'Id persona: {self.__id_persona}, '
            f'Nombre: {self.__nombre}, '
            f'Apellidos: {self.__apellidos}, '
            f'Email: {self.__email}'
        )

    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona
    
    def get_id_persona(self):
        return self.__id_persona
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
        
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
    
    def get_apellidos(self):
        return self.__apellidos
    
    def set_email(self, email):
        self.__email = email
    
    def get_email(self):
        return self.__email

if __name__ == '__main__':
    persona1 = Persona(nombre='Juan', apellidos='Perez', email='email')
    logger.debug(persona1)
