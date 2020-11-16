import psycopg2

# Conexion
conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#conexion.autocommit = True Hace el coomit en automatico. Solo en desarrollo
try:
    cursor = conexion.cursor()
    sql = 'INSERT INTO persona (nombre, apellidos, email) VALUES (%s, %s, %s)'
    valores = ('Carlos','Fernandez', 'cfernadez@mail.com')
    cursor.execute(sql, valores)

    sql = 'UPDATE persona SET nombre = %s, apellidos = %s, email =%s WHERE id_persona = %s' 
    valores = ('Karlos','Delgado', 'karlos.delgado@mail.com', 9)
    cursor.execute(sql, valores)
    # guardamos la informacion en la base de datos
    conexion.commit()
except Exception as e:
    #rollback da marchar atras a todas las opeaciones pendientes
    conexion.rollback()
    print(f'Ocurrio un error en la trasacción: {e}')
finally:
    cursor.close()
    conexion.close()