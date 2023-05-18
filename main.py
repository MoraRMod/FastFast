from client import Client
from date import Date
from hour import Hour
from product import Product
from supplier import Supplier
from employee import Employee
from ticket import Ticket
from bill import Bill

prueba = []
hora = Hour('09', '45')
fecha = Date('17', '05', '2023')
nombre = Employee()
producto = Product()
cliente = Client()

nombre.setName('Omar')
producto.setName('Galletas')
cliente.setName('Yair')

prueba = Bill(hora, fecha, nombre.getName(), producto.getName(), cliente.getName())

print(prueba)