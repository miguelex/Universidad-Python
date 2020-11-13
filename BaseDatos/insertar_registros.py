import psycopg2

# Conexion
conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sql = 'INSERT INTO persona (nombre, apellidos, email) VALUES (%s, %s, %s)'
valores = (('Maria','Gonzalez', 'maria.gonzzlez@mail.com'),
           ('Angel','Fernandez', 'afernadez@mail.com'),
           ('Javi','Poley', 'japogo@mail.com')
        )
cursor.executemany(sql, valores)

# guardamos la informacion en la base de datos
conexion.commit()

registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')
cursor.close()
conexion.close()