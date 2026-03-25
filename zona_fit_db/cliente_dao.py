from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    INSERTAR = "INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)"
    ACTUALIZAR = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM cliente WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                # print(cliente)
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Error al seleccionar clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount#Valores modificados en la base de datos
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount#Valores modificados en la base de datos
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

# Pruebas
if __name__ == "__main__":
    # # Insertar clientes
    # print("-"*50)
    # cliente1 = Cliente(nombre="Juan", apellido="Perez", membresia=300)
    # clientes_actualizados = ClienteDAO.insertar(cliente1)
    # print(f"Clientes insertados: {clientes_actualizados}")
    # print("-"*50)
    #Actualizar CLiente
    cliente_actualizar = Cliente(2,"Alexa", "Perez", 600)
    clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    print(f"Clientes actualizados: {clientes_actualizados}")
    # seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)