class Date:
	# Agrega datos por clase
	def __init__(self, day = "", month = "", year = "") -> None:
		self.__day = day
		self.__month = month
		self.__year = year
	# toString de la clase
	def __str__(self) -> str:
		return f"{self.__day}/{self.__month}/{self.__year}"
	
	# Guardar en disco
	def toDict(self):
		return {
			"day": self.__day,
			"month": self.__month,
			"year": self.__year
		}
	
	# SETTERS
	def setDay(self, day):
		self.__day = day
	
	def setMonth(self, month):
		self.__month = month
	
	def setYear(self, year):
		self.__year = year

	# GETTERS
	def getDay(self):
		return self.__day

	def getMonth(self):
		return self.__month

	def getYear(self):
		return self.__year