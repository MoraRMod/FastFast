def generarTicket(id, empleado, hora, fecha, productos, metodoPago):
	print("************************************")
	print("         TICKET DE COMPRA      ")
	print("************************************")
	print(f"ID: {id}")
	print(f"Empleado: {empleado}")
	print(f"Hora: {hora}")
	print(f"Fecha: {fecha}")
	print("----------------------------")
	total = 0
	for producto in productos:
		codigo = producto.getCode()
		nombre = producto.getName()
		precio = int(producto.getUnitaryValue())
		print(f"Código del producto: {codigo}")
		print(f"Producto: {nombre}")
		print(f"Precio: {precio}")
		print("----------------------------")
		total += int(precio)
	print(f"Total: {total}")
	print(f"Método de pago: {metodoPago}")
	print("************************************")

def generarFactura(hora, fecha, empleado, cliente, productos, metodoPago):
	print("====================================")
	print("              FACTURA             ")
	print("====================================\n")

	print(f"Fecha de Facturación: {fecha}")
	print(f"Hora de Facturación: {hora}\n")

	print("------------------------------------")
	print("Información del Vendedor:")
	print(f"Nombre: {empleado.getName()}")
	print(f"RFC: {empleado.getRFC()}")
	print(f"Dirección: {empleado.getAddress()}")
	print(f"Email: {empleado.getMail()}")
	print(f"Teléfono: {empleado.getPhoneNumber()}\n")

	print("------------------------------------")
	print("Información del Cliente:")
	print(f"ID: {cliente.getID()}")
	print(f"Nombre: {cliente.getName()}")
	print(f"RFC: {cliente.getRFC()}")
	print(f"Email: {cliente.getMail()}")
	print(f"Teléfono: {cliente.getPhoneNumber()}\n")

	print("------------------------------------")
	print("Productos:")

	subtotal = 0

	for index, producto in enumerate(productos, 1):
		print(f"{index}. Producto: {producto.getName()}")
		print(f"   Código: {producto.getCode()}")
		print(f"   Precio unitario: ${producto.getUnitaryValue()}")
		print(f"   Cantidad: {producto.getStock()}")

		totalProducto = int(producto.getUnitaryValue()) * int(producto.getStock())
		subtotal += totalProducto

		print(f"   Total: ${totalProducto}\n")

	impuesto = subtotal * 0.16
	total = subtotal + impuesto

	print("------------------------------------")
	print(f"Subtotal: ${subtotal}")
	print(f"Impuesto (IVA 16%): ${impuesto}")
	print(f"Total: ${total}\n")

	print("------------------------------------")
	print(f"Método de Pago: {metodoPago}\n")

	print("====================================")