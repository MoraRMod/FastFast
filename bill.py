class Bill:
	# Agrega datos por clase
	def __init__(self, broadcastHour = None, broadcastDate = None, nameEmployee = "", nameProduct = "", nameClient = "") -> None:
		self.__broadcastHour = broadcastHour
		self.__broadcastDate = broadcastDate
		self.__nameEmployee = nameEmployee
		self.__nameProduct = nameProduct
		self.__nameClient = nameClient
	# toString de la clase
	def __str__(self) -> str:
		return(
			"Hora: " + str(self.__broadcastHour) + "\n" +
			"Fecha: " + str(self.__broadcastDate) + "\n" +
			"Empleado: " + str(self.__nameEmployee) + "\n" +
			"Producto: " + str(self.__nameProduct) + "\n" +
			"Nombre del cliente: " + str(self.__nameClient)
		)
	# Guardar en disco
	def toDict(self):
		return {
			"broadcastHour": self.__broadcastHour.toDict() if self.__broadcastHour else None,
			"broadcastDate": self.__broadcastDate.toDict() if self.__broadcastDate else None,
			"nameEmployee": self.__nameEmployee,
			"nameProduct": self.__nameProduct,
			"nameClient": self.__nameClient
		}
	
	# SETTERS
	def setNameClient(self, nameClient):
		self.__nameClient = nameClient
	
	# GETTERS
	def getBroadcastHour(self):
		return self.__broadcastHour

	def getBroadcastDate(self):
		return self.__broadcastDate

	def getNameEmployee(self):
		return self.__nameEmployee
	
	def getNameProduct(self):
		return self.__nameProduct
	
	def getNameClient(self):
		return self.__nameClient