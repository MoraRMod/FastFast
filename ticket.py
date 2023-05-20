class Ticket:
	# Agrega datos por clase
	def __init__(self, id = "", employee = "", hour = None, date = None, productCode = "", productName = "", productValue = "", methodPayment = "") -> None:
		self.__id = id
		self.__employee = employee
		self.__hour = hour
		self.__date = date
		self.__productCode = productCode
		self.__productName = productName
		self.__productValue = productValue
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
			"Producto: " + str(self.__productName) + "\n" +
			"Precio: " + str(self.__productValue) + "\n" +
			"Método de pago: " + str(self.__methodPayment)
		)
	# Guardar en disco
	def toDict(self):
		return {
			"id": self.__id,
			"employee": self.__employee,
			"hour": self.__hour.toDict() if self.__hour else None,
			"date": self.__date.toDict() if self.__date else None,
			"productCode": self.__productCode,
			"productName": self.__productName,
			"productValue": self.__productValue,
			"methodPayment": self.__methodPayment
		}
	
	# SETTERS
	def setID(self, id):
		self.__id = id

	def setHour(self, hour):
		self.__hour = hour

	def setDate(self, date):
		self.__date = date
	
	def setEmployee(self, employee):
		self.__employee = employee

	def setProductCode(self, productCode):
		self.__productCode = productCode

	def setProductName(self, productName):
		self.__productName = productName
	
	def setProductValue(self, productValue):
		self.__productValue = productValue

	def setMethodPayment(self, methodPayment):
		self.__methodPayment = methodPayment
	
	# GETTERS
	def getID(self):
		return self.__id
	
	def getHour(self):
		return self.__hour
	
	def getDate(self):
		return self.__date

	def getEmployee(self):
		return self.__employee

	def getProductCode(self):
		return self.__productCode

	def getProductName(self):
		return self.__productName
	
	def getProductValue(self):
		return self.__productValue
	
	def getMethodPayment(self):
		return self.__methodPayment
