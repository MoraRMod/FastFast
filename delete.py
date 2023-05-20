from searches import findID, findCode, findNameSupplier

def eliminarRegistro(gerente, id):
	resultados = findID(gerente, id)

	if resultados:
		print(f"Resultados de la búsqueda para el ID '{id}':")
		
		for registro in resultados:
			for obj in registro:
				print(obj)
			print('\n')

		gerente.eliminar(resultados[0])

		print("Registro eliminado.")
	else:
		print(f"No se encontraron resultados para el ID '{id}'.")

def eliminarCode(gerente, code):
	resultados = findCode(gerente, code)

	if resultados:
		print(f"Resultados de la búsqueda para el codigo '{code}':")
		
		for registro in resultados:
			for obj in registro:
				print(obj)
			print('\n')

		gerente.eliminar(resultados[0])

		print("Producto eliminado.")
	else:
		print(f"No se encontraron resultados para el codigo '{code}'.")

def eliminarProoveedor(gerente, name):
	resultados = findNameSupplier(gerente, name)

	if resultados:
		print(f"Resultados de la búsqueda para el prooveedor '{name}':")
		
		for registro in resultados:
			for obj in registro:
				print(obj)
			print('\n')

		gerente.eliminar(resultados[0])

		print("Registro eliminado.")
	else:
		print(f"No se encontraron resultados para el prooveedor '{name}'.")