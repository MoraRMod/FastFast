class Supplier:
	# Agrega datos por clase
	def __init__(self, name = "", address = "", mail = "", phoneNumber = "") -> None:
		self.__name = name
		self.__address = address
		self.__mail = mail
		self.__phoneNumber = phoneNumber
	# toString de la clase
	def __str__(self) -> str:
		return(
			"Nombre: " + str(self.__name) + "\n" +
			"Dirección: " + str(self.__address) + "\n" +
			"Correo: " + str(self.__mail) + "\n" +
			"Número de teléfono: " + str(self.__phoneNumber)
		)
	# Guardar en disco
	def toDict(self):
		return {
			"name": self.__name,
			"address": self.__address,
			"mail": self.__mail,
			"phoneNumber": self.__phoneNumber,
		}
	
	# SETTERS
	def setName(self, name):
		self.__name = name
	
	def setAddress(self, address):
		self.__address = address
	
	def setMail(self, mail):
		self.__mail = mail

	def setPhoneNumber(self, phoneNumber):
		self.__phoneNumber = phoneNumber
	
	# GETTERS
	def getName(self):
		return self.__name

	def getAddress(self):
		return self.__address

	def getMail(self):
		return self.__mail

	def getPhoneNumber(self):
		return self.__phoneNumber