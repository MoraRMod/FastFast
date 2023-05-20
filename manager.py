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

	def getList(self):
		return self.__gerente

	def mostrar(self):
		for i in range(len(self.__gerente)):
			print(f'Índice {i}')

			for obj in self.__gerente[i]:
				print(obj)

			print("\n")

	def actualizarRegistro(self, registro):
		for i in range(len(self.__gerente)):
			if self.__gerente[i][0] == registro[0]:
				self.__gerente[i] = registro
				break
	
	def actualizarProducto(self, registro):
		for i in range(len(self.__gerente)):
			if self.__gerente[i][3] == registro[3]:
				self.__gerente[i] = registro
				break
	
	def actualizarProoveedor(self, registro):
		for i in range(len(self.__gerente)):
			if self.__gerente[i][4] == registro[4]:
				self.__gerente[i] = registro
				break
	
	def eliminar(self, registro):
		self.__gerente.remove(registro)


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
		if self.cont < len(self.__gerente):
			quark = self.__gerente[self.cont]

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

				self.__gerente = [
					[
						Hour(element[2]['hour'], element[2]['minute']),
						Date(element[1]['day'], element[1]['month'], element[1]['year']),
						Product(element[3]['stock'], element[3]['unitaryValue'], element[3]['name'], element[3]['code']),
						Supplier(element[4]['name'], element[4]['address'], element[4]['mail'], element[4]['phoneNumber']),
						Client(element[0]['id'], element[0]['name'], element[0]['rfc'], element[0]['phoneNumber'], element[0]['mail']),
						Employee(element[5]['id'], element[5]['birthday'], element[5]['name'], element[5]['address'], element[5]['rfc'], element[5]['mail'], element[5]['phoneNumber']),
						Ticket(element[6]['id'], element[6]['employee'], element[6]['hour'], element[6]['date'], element[6]['productCode'], element[6]['product'], element[6]['methodPayment']),
						Bill(element[7]['broadcastHour'], element[7]['broadcastDate'], element[7]['nameEmployee'], element[7]['nameProduct'], element[7]['nameClient'])
					]
					for element in lista
				]

				return 1
		except Exception as e:
			print(f"Error al abrir archivo: {e}")
			return 0