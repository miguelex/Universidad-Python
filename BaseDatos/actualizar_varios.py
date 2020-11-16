import psycopg2

# Conexion
conexion = psycopg2.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')

cursor = conexion.cursor()
sentencia = 'UPDATE persona SET nombre = %s, apellidos = %s, email = %s WHERE id_persona = %s'
valores = (
    ('Juan', 'Perez', 'jperez@mail.com', 8),
    ('Karla1', 'Gomez2', 'kgomez3@mail.com', 2)
)
cursor.executemany(sentencia, valores)

# guardamos la informacion en la base de datos
conexion.commit()

registros_actualizados = cursor.rowcount
print(f'Registros insertados: {registros_actualizados}')
cursor.close()
conexion.close()
