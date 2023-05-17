class Product:
	# Agrega datos por clase
	def __init__(self, stock = "", unitaryValue = "", name = "", code = "") -> None:
		self.__stock = stock
		self.__unitaryValue = unitaryValue
		self.__name = name
		self.__code = code
	# toString de la clase
	def __str__(self) -> str:
		return(
			"Existencia: " + str(self.__stock) + "\n" +
			"Precio unitario: " + str(self.__unitaryValue) + "\n" +
			"Nombre: " + str(self.__name) + "\n" +
			"Código: " + str(self.__code)
		)
	# SETTERS
	def setStock(self, stock):
		self.__stock = stock
	
	def setUnitaryValue(self, unitaryValue):
		self.__unitaryValue = unitaryValue
	
	def setName(self, name):
		self.__name = name

	def setCode(self, code):
		self.__code = code
	
	# GETTERS
	def getStock(self):
		return self.__stock

	def getUnitaryValue(self):
		return self.__unitaryValue

	def getName(self):
		return self.__name

	def getCode(self):
		return self.__code