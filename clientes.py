import os
import json


def agregar_cliente(nombre, apellido, cuit, domicilio):
    pathname = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(pathname, "clientes.json")
    with open(pathname, "r") as file:
        clientes = json.load(file)
    if len(clientes)<1:
        id = 0 
    else:
        max_id = max(clientes, key=lambda a: a["id"])
        id = max_id["id"] + 1
    clientes.append({"id": id, "nombre": nombre, "apellido": apellido, "cuit":  cuit, "domicilio": domicilio})
    with open(pathname, "w") as file:
        json.dump(clientes, file, indent=4)


def editar_cliente(id_cliente):
    cliente = devolver_cliente_por_id(id_cliente)
    lista_clientes = devolver_clientes()
    lista_clientes.remove(cliente)
    nombre = str(input('Ingrese el nombre: '))
    apellido = str(input('Ingrese el apellido: '))
    cuit = int(input('Ingrese el CUIT/CUIL: '))
    domicilio = str(input('Ingrese el domicilio: '))
    lista_clientes.append({"id": id_cliente, "nombre": nombre, "apellido": apellido, "cuit": cuit, "domicilio": domicilio })
    ordenado = sorted(lista_clientes, key=lambda a: a["id"])
    pathname = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(pathname, "clientes.json")
    with open(pathname, "w") as file:
         json.dump(ordenado, file, indent=4)
       


def devolver_clientes():
    pathname = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(pathname, "clientes.json")
    with open(pathname, "r") as file:
        clientes = json.load(file)
    return clientes

def eliminar_cliente(id):
    cliente = devolver_cliente_por_id(id)
    lista_clientes = devolver_clientes()
    lista_clientes.remove(cliente)
    pathname = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(pathname, "clientes.json")
    with open(pathname, "w") as file:
        json.dump(lista_clientes, file, indent=4)


def devolver_cliente_por_id(id):
    clientes = devolver_clientes()
    for cliente in clientes:
        if cliente["id"] == int(id):
            return cliente
    return False


