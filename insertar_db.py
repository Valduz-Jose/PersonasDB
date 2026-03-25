#insertar registros en la base de datos
import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',#127.0.0.1
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre,apellido,edad) VALUES (%s,%s,%s)'
valores = ('Juan','Contreras',19)
cursor.execute(sentencia_sql,valores)
personas_db.commit() #confirmar los cambios en la base de datos

print(f'Se ha agregado el registro: {valores}')

cursor.close()
personas_db.close()
