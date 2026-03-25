#ACtualizar registros en la base de datos
import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',#127.0.0.1
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores=('Victoria','Flores',45,6)
cursor.execute(sentencia_sql,valores)
personas_db.commit()#Confirma los cambios en la base de datos
print("Se ha actualizado la informacion")
cursor.close()
personas_db.close()