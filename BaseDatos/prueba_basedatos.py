import psycopg2

# Conexion
conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sql = 'SELECT * FROM persona'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()


