class Hour:
	# Agrega datos por clase
	def __init__(self, hour = "", minute = "") -> None:
		self.__hour = hour
		self.__minute = minute
	# toString de la clase
	def __str__(self) -> str:
		return f"{self.__hour}:{self.__minute}"
	# Guardar en disco
	def toDict(self):
		return {
			"hour": self.__hour,
			"minute": self.__minute
		}

	# SETTERS

	def setHour(self, hour):
		self.__hour = hour

	def setMinute(self, minute):
		self.__minute = minute

	# GETTERS
	def getHour(self):
		return self.__hour
	
	def getMinute(self):
		return self.__minute