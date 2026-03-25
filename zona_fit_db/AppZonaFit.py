from cliente_dao import ClienteDAO
from cliente import Cliente


print("**** CLientes Zona Fit Gym ****")

opcion = None
while opcion != 5:
    print("""Menu:
    1. Listar Clientes
    2. Agregar Cliente
    3. Actualizar Cliente
    4. Eliminar Cliente
    5. Salir
    """)
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:#Listar clientes
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de CLientes ***')
        for cliente in clientes:
            print(cliente)
    elif opcion == 2:#Agregar cliente
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        membresia = int(input("Ingrese el valor de la membresia: "))
        cliente_nuevo = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        clientes_insertados = ClienteDAO.insertar(cliente_nuevo)
        print(f"Clientes insertados: {clientes_insertados}")

    elif opcion == 3:#Actualizar cliente
        id_cliente = int(input("Ingrese el ID del cliente a actualizar: "))
        nombre = input("Ingrese el nuevo nombre del cliente: ")
        apellido = input("Ingrese el nuevo apellido del cliente: ")
        membresia = int(input("Ingrese el nuevo valor de la membresia: "))
        cliente_actualizar = Cliente(id=id_cliente, nombre=nombre, apellido=apellido, membresia=membresia)
        clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
        print(f"Clientes actualizados: {clientes_actualizados}")

    elif opcion == 4:#Eliminar cliente
        id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
        cliente_eliminar = Cliente(id=id_cliente)
        clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
        print(f"Clientes eliminados: {clientes_eliminados}")
else:
    print("Saliendo del programa...")