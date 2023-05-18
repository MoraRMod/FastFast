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

	def agregar(self, hour:Hour, date:Date, product:Product, supplier:Supplier, client:Client, employee:Employee, ticket:Ticket, bill:Bill):
		self.__gerente.append(hour)
		self.__gerente.append(date)
		self.__gerente.append(product)
		self.__gerente.append(supplier)
		self.__gerente.append(client)
		self.__gerente.append(employee)
		self.__gerente.append(ticket)
		self.__gerente.append(bill)

	def mostrar(self):
		print("ola")

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
		
	#agregar funciones de abrir y guardar archivo.