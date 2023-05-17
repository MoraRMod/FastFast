from hour import Hour
from date import Date

class Ticket:
	# Agrega datos por clase
	def __init__(self, id = "", employee = "", hour = Hour(), date = Date(), productCode = "", product = "", methodPayment = "") -> None:
		self.__id = id
		self.__employee = employee
		self.__hour = hour
		self.__date = date
		self.__productCode = productCode
		self.__product = product
		self.__methodPayment = methodPayment
	# Comparacion en caso de ordenamiento por ID
	def __lt__(self, other):
		self.__id < other.__id
	# toString de la clase
	def __str__(self) -> str:
		return(
			"Identificador: " + str(self.__id) + "\n" +
			"Empleado: " + str(self.__employee) + "\n" +
			"Hora: " + str(self.__hour) + "\n" +
			"Fecha: " + str(self.__date) + "\n" +
			"Código del producto: " + str(self.__productCode) + "\n" +
			"Producto: " + str(self.__product) + "\n" +
			"Método de pago: " + str(self.__methodPayment)
		)
	# SETTERS
	def setID(self, id):
		self.__id = id
	
	def setEmployee(self, employee):
		self.__employee = employee

	def setProductCode(self, productCode):
		self.__productCode = productCode

	def setProduct(self, product):
		self.__product = product

	def setMethodPayment(self, methodPayment):
		self.__methodPayment = methodPayment
	
	# GETTERS
	@property
	def getID(self):
		return self.__id

	@property
	def getEmployee(self):
		return self.__employee

	@property
	def getHour(self):
		return self.__hour
	
	@property
	def getDate(self):
		return self.__date

	@property
	def getProductCode(self):
		return self.__productCode

	@property
	def getProduct(self):
		return self.__product
	
	@property
	def getMethodPayment(self):
		return self.__methodPayment