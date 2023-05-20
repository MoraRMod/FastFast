from searches import findID

def eliminarRegistro(gerente, id):
	resultados = findID(gerente, id)

	if resultados:
		print(f"Resultados de la búsqueda para el ID '{id}':")
		
		for registro in resultados:
			for obj in registro:
				print(obj)
			print('\n')

		# Eliminar el registro de la lista de gerente
		gerente.eliminarRegistro(resultados[0])

		print("Registro eliminado.")
	else:
		print(f"No se encontraron resultados para el ID '{id}'.")