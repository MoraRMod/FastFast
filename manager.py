from hour import Hour
from date import Date
from product import Product
from supplier import Supplier
from client import Client
from employee import Employee
from ticket import Ticket
from bill import Bill
import json

class Manager:
	def __init__(self) -> None:
		self.__gerente = []

	def agregar(self, *args):
		self.__gerente.extend(args)

	def mostrar(self):
		for i in range(len(self.__gerente)):
			print(f'Índice {i}')

			for obj in self.__gerente[i]:
				print(obj)

			print("\n")

	def getIndex(self, index):
		return self.__gerente[index]
	
	def __len__(self):
		return(
			len(self.__gerente)
		)
	
	def __iter__(self):
		self.cont = 0

		return self
	
	def __next__(self):
		if self.cont < len(self.__cumulos):
			quark = self.__cumulos[self.cont]

			self.cont += 1

			return quark
		else:
			raise StopIteration
	
		
	def guardar(self, ubicacion):
		try:
			with open(ubicacion, 'w') as archivo:
				lista = [[hour.toDict(), date.toDict(), product.toDict(), supplier.toDict(), client.toDict(), employee.toDict(), ticket.toDict(), bill.toDict()] for hour, date, product, supplier, client, employee, ticket, bill in self.__gerente]

				print(lista)

				json.dump(lista, archivo, indent = 4)

				return 1
		except Exception as e:
			print(f"Error al guardar archivo: {e}")
            
			return 0
		
	def abrir(self, ubicacion):
		try:
			with open(ubicacion, 'r') as archivo:
				lista = json.load(archivo)

				self.__cumulos = [[Hour(**hour), Date(**date), Product(**product), Supplier(**supplier), Client(**client), Employee(**employee), Ticket(**ticket), Bill(**bill)] for hour, date, product, supplier, client, employee, ticket, bill in lista]

				return 1
		except Exception as e:
			print(f"Error al abrir archivo: {e}")
            
			return 0