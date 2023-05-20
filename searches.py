from client import Client
from product import Product
from supplier import Supplier

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

def findCode(gerente, code):
	resultado = []

	for registro in gerente.getList():
		for obj in registro:
			if isinstance(obj, Product) and obj.getCode() == code:
				resultado.append(registro)

	return resultado

def findNameSupplier(gerente, name):
	resultado = []

	for registro in gerente.getList():
		for obj in registro:
			if isinstance(obj, Supplier) and obj.getName() == name:
				resultado.append(registro)

	return resultado