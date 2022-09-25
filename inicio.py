import clientes
import comprobantes
import detalle
from datetime import date
from datetime import datetime

inicio = int(input('Presione \n1- Para ingresar a clientes. \n2- Para ingresar a comprobantes. \n0- Para salir. \n'))
while inicio != 0:
  
  #Ingresar a clientes
  if inicio == 1:
    inicio2 = str(input('Presione ENTER para continuar o escriba la palabra "fin" para finalizar : '))
    while inicio2 != 'fin':
        opcion = int(input('Elija una de las siguientes opciones:\n1- Registrar un cliente nuevo.\n2- Editar datos de un cliente existente. \n3- Eliminar un cliente: \n0- Para salir. \n'))
        while opcion != 0:
          
          #Registrar cliente nuevo
          if opcion == 1:
            nombre = input('Ingrese el nombre: ')
            apellido = input('Ingrese el apellido: ') 
            cuit = input('Ingrese el cuit: ') 
            domicilio = input('Ingrese el domicilio: ')
            agregar = clientes.agregar_cliente(nombre, apellido, cuit, domicilio)
            print("Cliente agregado!")
            opcion = int(input('Elija una de las siguientes opciones:\n1- Registrar un cliente nuevo.\n2- Editar datos de un cliente existente. \n3- Eliminar un cliente: \n0- Para salir. \n'))
      
          #Editar datos de cliente existente
          if opcion == 2:
            lista_clientes = clientes.devolver_clientes()
            print(f"ID - APELLIDO Y NOMBRE")
            for cliente in lista_clientes:
              print(f"{cliente['id']} - {cliente['apellido']} {cliente['nombre']}")
            id_cliente = int(input('Ingrese el ID del cliente a editar: '))
            editar = clientes.editar_cliente(id_cliente)
            clientes_actualizado = clientes.devolver_clientes()
            print("Cliente editado con éxito!")
            print(clientes_actualizado)
            opcion = int(input('Elija una de las siguientes opciones:\n1- Registrar un cliente nuevo.\n2- Editar datos de un cliente existente. \n3- Eliminar un cliente: \n0- Para salir. \n'))
              
          #Eliminar un cliente
          if opcion == 3:
            lista_clientes = clientes.devolver_clientes()
            print(f"ID - APELLIDO Y NOMBRE")
            for cliente in lista_clientes:
              print(f"{cliente['id']} - {cliente['apellido']} {cliente['nombre']}")
            eliminar = int(input('Ingrese el ID del cliente a eliminar: '))
            clientes.eliminar_cliente(eliminar)
            print("Cliente eliminado!")
            opcion = int(input('Elija una de las siguientes opciones:\n1- Registrar un cliente nuevo.\n2- Editar datos de un cliente existente. \n3- Eliminar un cliente: \n0- Para salir. \n'))
        inicio2 = str(input('Presione ENTER para continuar o escriba la palabra "fin" para finalizar : '))


  #Ingresar a comprobantes
  if inicio == 2:
      opcionescomp = int(input('Presione \n1- Para agregar un nuevo comprobante. \n2- Para buscar un antiguo comprobante. \n0- Para finalizar. \n'))
      while opcionescomp != 0:
        
        #Agregar nuevo comprobante
        if opcionescomp == 1:
          lista_clientes = clientes.devolver_clientes()
          print(f"ID - APELLIDO Y NOMBRE")
          for cliente in lista_clientes:
            print(f"{cliente['id']} - {cliente['apellido']} {cliente['nombre']}")
          cliente_id = input('Selecciones el ID del cliente al que desea generarle el comprobante: ')
          cliente = clientes.devolver_cliente_por_id(cliente_id)
          if cliente:
              #Corroborar datos de factura
              tipo = str(input('Ingrese el tipo de factura, A, B o C: '))
              while tipo != 'A' and tipo != 'B' and tipo != 'C':
                print('Por favor ingrese un tipo válido de factura A, B o C')
                tipo = str(input('Ingrese el tipo de factura, A, B o C: '))
              punto = int(input('Por favor ingrese el punto de venta: ')[0:4])
              punto_de_venta = comprobantes.completa_ceros(punto, 4)
              opcion = input('Presione ENTER para un nuevo detalle o 0 para salir. \n')
              lista_detalles = []
              while opcion != '0':
                #Datos de lista
                producto = str(input('Ingrese el nombre del producto: '))
                cantidad = int(input('Ingrese la cantidad comprada: '))
                precio = int(input('Ingrese el precio unitario del producto: '))
                while precio <= 0:
                  print('Por favor ingrese un precio válido!')
                  precio = int(input('Ingrese el precio unitario del producto: '))
                total = detalle.calculo_total(precio, cantidad)
                lista_detalles.append({"producto": producto, "cantidad": cantidad, "precio": precio, "total": total})
                opcion = input('Presione ENTER para un nuevo detalle o 0 para salir. \n')
                importe_total = comprobantes.importe_total_comprobante(lista_detalles)
              else:
                comprobantes.agregar_comprobante(cliente_id, tipo, punto_de_venta, lista_detalles, importe_total)
              print("Comprobante agregado con éxito!")
          else:
            print('ID no válido!')
            cliente_id = input('Selecciones el ID del cliente al que desea generarle el comprobante(Si el cliente no se encuentra en la lista, vuelva hacia atras para registarlo primero.): ')
        
        
        #Buscar comprobante
        if opcionescomp == 2:
          opciones_filtro = int(input('Elija que tipo de busqueda quiere realizar: \n1- Búsqueda por cliente. \n2- Búsqueda por rango de fechas. \n3- Búsqueda por producto. \n0- Para salir. \n'))
          while opciones_filtro != 0:
              
              #Búsqueda por cliente
              if opciones_filtro == 1:
                lista_clientes = clientes.devolver_clientes()
                print(f"ID - APELLIDO Y NOMBRE")
                for cliente in lista_clientes:
                  print(f"{cliente['id']} - {cliente['apellido']} {cliente['nombre']}")
                id_cliente = input('Ingrese el ID del cliente buscado: ')
                mostrar = comprobantes.buscar_por_cliente(id_cliente)
                cliente = clientes.devolver_cliente_por_id(id_cliente)
                print("\n",cliente)
                for i in mostrar:
                  print(f"\nFecha: {i['fecha']} - Tipo: {i['tipo']} - Punto de venta: {i['punto_de_venta']} - Numero de comprobante: {i['numero_de_comprobante']}")
                  for h in i['detalle']:
                    print(f"Producto: {h['producto']} - Cantidad: {h['cantidad']} - Precio: {h['precio']} - Total: {h['total']}")
                  print(f"Importe total: {i['importe_total']}\n")

              #Búsqueda por rango de fechas
              if opciones_filtro == 2:
                fecha_inicial = str(input('Ingrese la fecha desde la cual quiere filtrar(aaaa-mm-dd): '))
                fecha_final = str(input('Ingrese la fecha hasta la cual quiere filtrar(aaaa-mm-dd): '))
                fecha_desde = datetime.strptime(str(fecha_inicial), '%Y-%m-%d')
                fecha_hasta = datetime.strptime(str(fecha_final), '%Y-%m-%d')
                mostrar = comprobantes.filtrar_por_fecha(fecha_desde, fecha_hasta)
                for i in mostrar:
                  print(f"\nFecha: {i['fecha']} - Tipo: {i['tipo']} - Punto de venta: {i['punto_de_venta']} - Numero de comprobante: {i['numero_de_comprobante']}")
                  cliente = clientes.devolver_cliente_por_id(i['cliente_id'])
                  print("Datos del cliente: ",cliente)
                  for h in i['detalle']:
                    print(f"Producto: {h['producto']} - Cantidad: {h['cantidad']} - Precio: {h['precio']} - Total: {h['total']}")
                  print(f"Importe total: {i['importe_total']}\n")

              #Búsqueda por producto
              if opciones_filtro == 3:
                producto = str(input('Ingrese el nombre del producto para filtrar: '))
                devolver_producto = comprobantes.devolver_comprobantes_por_producto(producto)
                print (producto)
                for i in devolver_producto:
                  print(f"\nFecha: {i['fecha']} - Tipo: {i['tipo']} - Punto de venta: {i['punto_de_venta']} - Numero de comprobante: {i['numero_de_comprobante']}")
                  cliente = clientes.devolver_cliente_por_id(i['cliente_id'])
                  print("Datos del cliente:",cliente)
                  for h in i['detalle']:
                    print(f"Producto: {h['producto']} - Cantidad: {h['cantidad']} - Precio: {h['precio']} - Total: {h['total']}")
                  print(f"Importe total: {i['importe_total']}\n")

              opciones_filtro = int(input('Elija que tipo de busqueda quiere realizar: \n1- Búsqueda por cliente. \n2- Búsqueda por rango de fechas. \n3- Búsqueda por producto. \n0- Para salir. \n'))
        opcionescomp = int(input('Presione \n1- Para agregar un nuevo comprobante. \n2- Para buscar un antiguo comprobante. \n0- Para finalizar. \n'))
  inicio = int(input('Presione \n1- Para ingresar a clientes. \n2- Para ingresar a comprobantes. \n0- Para salir. \n'))

      