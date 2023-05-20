from searches import findID, findCode, findNameSupplier
from client import Client
from product import Product
from supplier import Supplier

def modificarID(gerente, id, name, rfc, phoneNumber, mail):
	resultados = findID(gerente, id)

	if resultados:
		for registro in resultados:
			for obj in registro:
				if isinstance(obj, Client):
					obj.setName(name)
					obj.setRFC(rfc)
					obj.setPhoneNumber(phoneNumber)
					obj.setMail(mail)

					break
		print(f"Se ha modificado el registro con el ID '{id}'.")

		gerente.actualizarRegistro(resultados[0])
	else:
		print(f"No se encontraron resultados para el ID '{id}'.")

def modificarCode(gerente, stock, unitaryValue, name, code):
	resultados = findCode(gerente, code)

	if resultados:
		for registro in resultados:
			for obj in registro:
				if isinstance(obj, Product):
					obj.setStock(stock)
					obj.setUnitaryValue(unitaryValue)
					obj.setName(name)

					break
		print(f"Se ha modificado el producto con el codigo '{code}'.")

		gerente.actualizarProducto(resultados[0])
	else:
		print(f"No se encontraron producto para el codigo '{code}'.")

def modificarProoveedor(gerente, name, address, mail, phoneNumber):
	resultados = findNameSupplier(gerente, name)

	if resultados:
		for registro in resultados:
			for obj in registro:
				if isinstance(obj, Supplier):
					obj.setAddress(address)
					obj.setMail(mail)
					obj.setPhoneNumber(phoneNumber)

					break
		print(f"Se ha modificado el prooveedor con el nombre '{name}'.")

		gerente.actualizarProoveedor(resultados[0])
	else:
		print(f"No se encontraron prooveedor para el nombre '{name}'.")