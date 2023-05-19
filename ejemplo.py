from modules import *

# Registros de prueba
gerente = Manager()
index = 0

while index <= 0:
	# Registros de longitud fija y variable
	cliente = Client('102364', 'Omar', 'DOJA98DHHF9', '56 4651 7427', 'ralerwip@gmail.com')
	fecha = Date('17', '05', '2023')
	hora = Hour('09', '45')
	producto = Product('95', '17', 'Takis', '0110111011')
	proovedor = Supplier('Barcel', 'Primavera #63', 'ayudabarcel@ayuda.com', '54 8499 0008')
	empleado = Employee('948367', fecha, 'Daniel', '5 de mayo #92', 'KAJN15ENMI4', 'soyDani@gmail.com', '33 1594 8269')
	recibo = Ticket('492816', empleado.getName(), hora, fecha, producto.getCode(), producto.getName(), 'Tarjeta de credito')
	prueba = Bill(hora, fecha, empleado.getName(), producto.getName(), cliente.getName())
	gerente.agregar([cliente, fecha, hora, producto, proovedor, empleado, recibo, prueba])

	#gerente.mostrar()

	index += 1

gerente.guardar('registros.json')
gerente.abrir('registros.json')

gerente.mostrar()

'''
# Indice simple
elemento = getIndex(gerente, 1)
for obj in elemento:
	print(obj)
'''

'''
print("Indice simple: 1")
for obj in elemento:
	print(obj)
'''

'''
# Indice invertido
print('\n')
indiceI = actualizarIndiceInvertido(gerente)
mostrarIndiceInvertido(gerente, indiceI)
'''

'''
# Serializacion
serializar(gerente, 'gerente.pkl')

gerente_deserializado = deserializar('gerente.pkl')
'''

'''
# Dispersion
dispersar(gerente)
mostrarDispersado(gerente)
'''

'''
# Encriptacion
clave = generarClave()

gerenteBytes = pickle.dumps(gerente)
msg = encriptar(gerenteBytes, clave)

desEnBy = desencriptar(msg, clave)
desEn = pickle.loads(desEnBy)
'''

'''
# Compresion
comprimir(gerente)
descomprimir('gerente.zip')
'''