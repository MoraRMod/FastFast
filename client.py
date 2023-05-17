class Client:
	# Agrega datos por clase
	def __init__(self, id = "", name = "", rfc = "", phoneNumber = "", mail = "") -> None:
		self.__id = id
		self.__name = name
		self.__rfc = rfc
		self.__phoneNumber = phoneNumber
		self.__mail = mail
	# Comparacion en caso de ordenamiento por ID
	def __lt__(self, other):
		self.__id < other.__id
	# toString de la clase
	def __str__(self) -> str:
		return(
			"Identificador: " + str(self.__id) + "\n" +
			"Nombre: " + str(self.__name) + "\n" +
			"RFC: " + str(self.__rfc) + "\n" +
			"Número de teléfono: " + str(self.__phoneNumber) + "\n" +
			"Correo: " + str(self.__mail)
		)
	# SETTERS
	def setID(self, id):
		self.__id = id
	
	def setName(self, name):
		self.__name = name
	
	def setRFC(self, rfc):
		self.__rfc = rfc

	def setPhoneNumber(self, phoneNumber):
		self.__phoneNumber = phoneNumber

	def setMail(self, mail):
		self.__mail = mail
	
	# GETTERS
	def getID(self):
		return self.__id

	def getName(self):
		return self.__name

	def getRFC(self):
		return self.__rfc

	def getPhoneNumber(self):
		return self.__phoneNumber
	
	def getMail(self):
		return self.__mail