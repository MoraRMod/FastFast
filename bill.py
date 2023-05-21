class Bill:
	# Agrega datos por clase
	def __init__(self, broadcastHour = None, broadcastDate = None, employee = None, product = None, client = None) -> None:
		self.__broadcastHour = broadcastHour
		self.__broadcastDate = broadcastDate
		self.__employee = employee
		self.__product = product
		self.__client = client
	# toString de la clase
	def __str__(self) -> str:
		return(
			"Hora: " + str(self.__broadcastHour) + "\n" +
			"Fecha: " + str(self.__broadcastDate) + "\n" +
			"Empleado: \n" + str(self.__employee) + "\n" +
			"Producto: \n" + str(self.__product) + "\n" +
			"Cliente: \n" + str(self.__client)
		)
	# Guardar en disco
	def toDict(self):
		return {
			"broadcastHour": self.__broadcastHour.toDict() if self.__broadcastHour else None,
			"broadcastDate": self.__broadcastDate.toDict() if self.__broadcastDate else None,
			"employee": self.__employee.toDict() if self.__employee else None,
			"product": self.__product.toDict() if self.__product else None,
			"client": self.__client.toDict() if self.__client else None
		}
	
	# SETTERS
	def setClient(self, client):
		self.__client = client
	
	# GETTERS
	def getBroadcastHour(self):
		return self.__broadcastHour

	def getBroadcastDate(self):
		return self.__broadcastDate

	def getEmployee(self):
		return self.__employee
	
	def geteProduct(self):
		return self.__product
	
	def getClient(self):
		return self.__client