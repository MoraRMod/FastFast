class Hour:
	# Agrega datos por clase
	def __init__(self, minute = "", hour = "") -> None:
		self.__minute = minute
		self.__hour = hour
	# toString de la clase
	def __str__(self) -> str:
		return f"{self.__minute}:{self.__hour}"
	# Guardar en disco
	def toDict(self):
		return {
			"minute": self.__minute,
			"hour": self.__hour
		}

	# SETTERS
	def setMinute(self, minute):
		self.__minute = minute
	
	def setHour(self, hour):
		self.__hour = hour

	# GETTERS
	def getMinute(self):
		return self.__minute

	def getHour(self):
		return self.__hour