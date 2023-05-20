from modules import *

# Registros de prueba
gerente = Manager()
index = 0

while index <= 1:
	# Registros de longitud fija y variable
	cliente = Client('102364', 'Omar', 'DOJA98DHHF9', '56 4651 7427', 'ralerwip@gmail.com')
	fecha = Date('17', '05', '2023')
	hora = Hour('09', '45')
	producto = Product('95', '17', 'Takis', '0110111011')
	proovedor = Supplier('Barcel', 'Primavera #63', 'ayudabarcel@ayuda.com', '54 8499 0008')
	empleado = Employee('948367', fecha, 'Daniel', '5 de mayo #92', 'KAJN15ENMI4', 'soyDani@gmail.com', '33 1594 8269')
	recibo = Ticket('492816', empleado.getName(), hora, fecha, producto.getCode(), producto.getName(), producto.getUnitaryValue(), 'Tarjeta de credito')
	prueba = Bill(hora, fecha, empleado.getName(), producto.getName(), cliente.getName())
	gerente.agregar([cliente, fecha, hora, producto, proovedor, empleado, recibo, prueba])

	#gerente.mostrar()
		
	index += 1

	gerente.generarTicketCompra(recibo.getID(), empleado.getName(), hora, fecha, producto.getCode(), producto.getName(), producto.getUnitaryValue(), recibo.getMethodPayment())

'''
id = '102364'
eliminarRegistro(gerente, id)

print('\n\n')
print('\n\n')

gerente.mostrar()
'''

'''
id_modificar = '102364'
nuevo_nombre = 'Juan'
nuevo_rfc = 'RGSK4645DS4'
nuevo_tel = '26498842'
nuevo_email = 'juan@example.com'

modificarID(gerente, id_modificar, nuevo_nombre, nuevo_rfc, nuevo_tel, nuevo_email)

print('\n\n')
gerente.mostrar()
'''

'''
id = '102364'
resultados = findID(gerente, id)

if resultados:
	print(f"Resultados de la búsqueda para el ID '{id}':")

	for registro in resultados:
		for obj in registro:
			print(obj)
		print('\n')
else:
	print(f"No se encontraron resultados para el ID '{id}'.")

print('\n\n')
'''

'''

nombre = 'Omar'
res = findName(gerente, nombre)

if res:
	print(f"Resultados de la búsqueda por nombre '{nombre}':")
	for registro in res:
		for obj in registro:
			print(obj)
else:
	print(f"No se encontraron resultados para el nombre '{nombre}'.")
'''

#gerente.mostrar()

#gerente.guardar('registros.json')
#gerente.abrir('registros.json')
#gerente.mostrar()

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