import os
import json
from datetime import date
from datetime import datetime

def agregar_ceros(num):
    return str(num+1).zfill(8)

def agregar_comprobante(cliente_id, tipo, punto_de_venta, detalle, importe_total):
    pathname = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(pathname, "comprobantes.json")
    with open(pathname, "r") as file:
        comprobantes = json.load(file)
    if len(comprobantes)<1:
        id = 0 
    else:
        max_id = max(comprobantes, key=lambda a: a["id"])
        id = max_id["id"] + 1
    numero_de_comprobante = agregar_ceros(id)
    fecha = str(date.today())
    comprobantes.append({"id": id, "cliente_id": cliente_id, "fecha": fecha, "tipo": tipo, "punto_de_venta": punto_de_venta, "numero_de_comprobante": numero_de_comprobante, "detalle": detalle, "importe_total": importe_total})
    with open(pathname, "w") as file:
        json.dump(comprobantes, file, indent=4)


def completa_ceros(num, cantidad):
    return str(num).zfill(cantidad)

def devolver_comprobantes():
    pathname = os.path.dirname(os.path.abspath(__file__))
    pathname = os.path.join(pathname, "comprobantes.json")
    with open(pathname, "r") as file:
        comprobantes = json.load(file)
    return comprobantes

def devolver_comprobante_por_id(id_comprobante):
    lista_comprobantes = devolver_comprobantes()
    for comprobante in lista_comprobantes:
        if comprobante["id"] == int(id_comprobante):
            return comprobante
    return False


def buscar_por_cliente(cliente_id):
    res = []
    lista = devolver_comprobantes()
    for comprobante in lista:
        if comprobante["cliente_id"] == cliente_id:
            res.append(comprobante)

    return res


def devolver_comprobantes_por_producto(producto):
    res = []
    lista = devolver_comprobantes()
    for comprobante in lista:
        detalle = comprobante["detalle"]
        for h in detalle:
         if h["producto"] == producto:
             res.append(comprobante)
    
    return res


def importe_total_comprobante(lista):
    res = 0
    for detalle in lista:
        res += detalle["total"]
    return res

def filtrar_por_fecha(fecha_desde, fecha_hasta):
    res = []
    comprobantes = devolver_comprobantes()
    for elem in comprobantes:
        fecha_date = datetime.strptime(elem['fecha'], '%Y-%m-%d')
        if fecha_date >= fecha_desde and fecha_date <= fecha_hasta:
            res.append(elem)
    return res
