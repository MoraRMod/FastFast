from date import Date

class Employee:
	# Agrega datos por clase
	def __init__(self, id = "", birthday = None, name = "", address = "", rfc = "", mail = "", phoneNumber = "") -> None:
		self.__id = id
		self.__birthday = birthday
		self.__name = name
		self.__address = address
		self.__rfc = rfc
		self.__mail = mail
		self.__phoneNumber = phoneNumber
	# Comparacion en caso de ordenamiento por ID
	def __lt__(self, other):
		self.__id < other.__id
	# toString de la clase
	def __str__(self) -> str:
		return(
			"Identificador: " + str(self.__id) + "\n" +
			"Cumpleaños: " + str(self.__birthday) + "\n" +
			"Nombre: " + str(self.__name) + "\n" +
			"Dirección: " + str(self.__address) + "\n" +
			"RFC: " + str(self.__rfc) + "\n" +
			"Correo: " + str(self.__mail) + "\n" +
			"Número de teléfono: " + str(self.__phoneNumber)
		)
	# Guardar en disco
	def toDict(self):
		return {
			"id": self.__id,
			"birthday": self.__birthday.toDict() if self.__birthday else None,
			"name": self.__name,
			"address": self.__address,
			"rfc": self.__rfc,
			"mail": self.__mail,
			"phoneNumber": self.__phoneNumber,
		}
	
	# SETTERS
	def setID(self, id):
		self.__id = id
		
	def setName(self, name):
		self.__name = name
	
	def setAddress(self, address):
		self.__address = address

	def setRFC(self, rfc):
		self.__rfc = rfc

	def setMail(self, mail):
		self.__mail = mail

	def setPhoneNumber(self, phoneNumber):
		self.__phoneNumber = phoneNumber
	
	# GETTERS
	def getID(self):
		return self.__id

	def getBirthday(self):
		return self.__birthday

	def getName(self):
		return self.__name

	def getAddress(self):
		return self.__address

	def getRFC(self):
		return self.__rfc

	def getMail(self):
		return self.__mail
	
	def getPhoneNumber(self):
		return self.__phoneNumber