import psycopg2

# Conexion
conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sql = 'UPDATE persona SET nombre = %s, apellidos = %s, email =%s WHERE id_persona = 8' 
valores = ('Karlos','Delgado', 'karlos.delgado@mail.com')
cursor.execute(sql, valores)

# guardamos la informacion en la base de datos
conexion.commit()

registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()