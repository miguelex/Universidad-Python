import psycopg2

# Conexion
conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sql = 'DELETE FROM persona WHERE id_persona = %s' 
valores = (8,)
cursor.execute(sql, valores)

# guardamos la informacion en la base de datos
conexion.commit()

refistros_eliminados = cursor.rowcount
print(f'Registros eliminados: {refistros_eliminados}')
cursor.close()
conexion.close()