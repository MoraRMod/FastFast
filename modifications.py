from searches import findID
from client import Client

def modificarID(gerente, id, newName, newRFC, newTel, newMail):
	resultados = findID(gerente, id)

	if resultados:
		for registro in resultados:
			for obj in registro:
				if isinstance(obj, Client):
					obj.setName(newName)
					obj.setRFC(newRFC)
					obj.setPhoneNumber(newTel)
					obj.setMail(newMail)

					break
		print(f"Se ha modificado el registro con ID '{id}'.")

		gerente.actualizarRegistro(resultados[0])
	else:
		print(f"No se encontraron resultados para el ID '{id}'.")