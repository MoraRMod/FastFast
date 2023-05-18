from client import Client
from date import Date
from hour import Hour
from product import Product
from supplier import Supplier
from employee import Employee
from ticket import Ticket
from bill import Bill
from manager import Manager

# Registros de prueba
gerente = Manager()
index = 0

while index <= 4:
	cliente = Client('102364', 'Omar', 'DOJA98DHHF9', '56 4651 7427', 'ralerwip@gmail.com')
	fecha = Date('17', '05', '2023')
	hora = Hour('09', '45')
	producto = Product('95', '17', 'Takis', '0110111011')
	proovedor = Supplier('Barcel', 'Primavera #63', 'ayudabarcel@ayuda.com', '54 8499 0008')
	empleado = Employee('948367', fecha, 'Daniel', '5 de mayo #92', 'KAJN15ENMI4', 'soyDani@gmail.com', '33 1594 8269')
	recibo = Ticket('492816', empleado.getName(), hora, fecha, producto.getCode(), producto.getName(), 'Tarjeta de credito')
	prueba = Bill(hora, fecha, empleado.getName(), producto.getName(), cliente.getName())
	gerente.agregar([cliente, fecha, hora, producto, proovedor, empleado, recibo, prueba])

	gerente.mostrar()

	index += 1

elemento = gerente.getIndex(1)

print("Indice 1")
for obj in elemento:
	print(obj)