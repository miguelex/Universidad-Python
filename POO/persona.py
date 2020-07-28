class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Modificar valores
Persona.nombre= "Juan"
Persona.edad = 28

#Acceder valores
print(Persona.nombre)
print(Persona.edad)

#Crear objeto
persona = Persona("Migue", 45)
print(persona.nombre)
print(persona.edad)
print(id(persona))

#Crear otro objeto
persona2 = Persona("Karla", 25)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))