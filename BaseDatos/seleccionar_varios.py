import psycopg2

# Conexion
conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sql = 'SELECT * FROM persona WHERE id_persona IN %s'
llaves_primarias = ((1,2,3),)

cursor.execute(sql, llaves_primarias)
registros = cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()