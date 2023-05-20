from client import Client

def findID(gerente, id):
	resultado = []

	for registro in gerente.getList():
		for obj in registro:
			if isinstance(obj, Client) and obj.getID() == id:
				resultado.append(registro)

	return resultado

def findName(gerente, nombre):
	resultado = []

	for registro in gerente.getList():
		for obj in registro:
			if isinstance(obj, Client) and obj.getName() == nombre:
				resultado.append(registro)

	return resultado