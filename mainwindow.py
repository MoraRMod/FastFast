from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot
from client import Client
import os
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("FastFast")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Definicion de los elementos principales
        self.customers = []
        self.customerRow = 0
        self.currentSelection = ""
        self.icon = True
        
        #Cambios a que se efectuan dentro del programa al ejecutarlo
        self.ui.FullWidget.setVisible(False)
        self.ui.buscarEmpleado_linea.setVisible(False)
        self.ui.ID_busqueda_label.setVisible(False)
        self.ui.busquedaClienteConfirm.setVisible(False)
        self.getFiles()
        
        #Cambios entre barras laterales
        self.ui.iconHome.clicked.connect(self.button_logic)
        self.ui.fullHome.clicked.connect(self.button_logic)
        
        #Logica de los botones de la barra lateral
        self.ui.iconFactura.clicked.connect(self.menu_logic)
        self.ui.iconPedido.clicked.connect(self.menu_logic)
        self.ui.iconAlimento.clicked.connect(self.menu_logic)
        self.ui.iconClientes.clicked.connect(self.menu_logic)
        self.ui.iconEmpleados.clicked.connect(self.menu_logic)
        self.ui.iconProveedor.clicked.connect(self.menu_logic)
        
        self.ui.fullFactura.clicked.connect(self.menu_logic)
        self.ui.fullPedido.clicked.connect(self.menu_logic)
        self.ui.fullAlimento.clicked.connect(self.menu_logic)
        self.ui.fullCliente.clicked.connect(self.menu_logic)
        self.ui.fullEmpleado.clicked.connect(self.menu_logic)
        self.ui.fullProveedor.clicked.connect(self.menu_logic)
        
        #Pantalla inicial
        self.ui.multipleMenu.setCurrentIndex(6)
        
        #Logica de clientes
        self.ui.addCliente.clicked.connect(self.addClienteWindow)
        self.ui.saveCliente.clicked.connect(self.saveCliente)
        self.ui.modifyCliente.clicked.connect(self.modifyClienteWindow)
        self.ui.modifyClienteConfirm.clicked.connect(self.modifyCliente)
        self.ui.deleteCliente.clicked.connect(self.deleteClienteWindow)
        self.ui.deleteClienteConfirm.clicked.connect(self.deleteClient)
        self.ui.searchCliente.clicked.connect(self.searchClienteWindow)
        self.ui.busquedaClienteConfirm.clicked.connect(self.searchCliente)
        self.ui.cleanCliente.clicked.connect(self.clearBusquedaCliente)
        self.ui.cancelOpCliente.clicked.connect(self.cancelClienteWindow)
        self.ui.cancelModifyCliente.clicked.connect(self.cancelClienteWindow)
        self.ui.cancelDeleteCliente.clicked.connect(self.cancelClienteWindow)
        self.ui.tablaClientes.itemSelectionChanged.connect(self.selectionOfCustomer)
        
        #Logica del texto de la alta de clientes
        self.ui.nameCliente.textChanged.connect(self.releaseSaveCliente)
        self.ui.RFCCliente.textChanged.connect(self.releaseSaveCliente)
        self.ui.phoneCliente.textChanged.connect(self.releaseSaveCliente)
        self.ui.mailCliente.textChanged.connect(self.releaseSaveCliente)
        
    def getFiles(self):
        dir_path = os.path.dirname(__file__)
        file_path = os.path.join(dir_path, "customers.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                self.customers = [Client(**customer) for customer in data]

    @Slot()
    def button_logic(self):
        if self.ui.fullHome.isChecked():
            self.ui.FullWidget.setVisible(False)
            self.ui.IconWidget.setVisible(True)
            
            self.ui.fullHome.setChecked(False)
            self.ui.iconHome.setChecked(False)
        elif self.ui.iconHome.isChecked():
            self.ui.IconWidget.setVisible(False)
            self.ui.FullWidget.setVisible(True)
            
            self.ui.iconHome.setChecked(False)
            self.ui.fullHome.setChecked(False)
            
    @Slot()
    def menu_logic(self):
        if self.ui.iconFactura.isChecked() or self.ui.fullFactura.isChecked():
            self.ui.multipleMenu.setCurrentIndex(0)
        elif self.ui.iconPedido.isChecked() or self.ui.fullPedido.isChecked():
            self.ui.multipleMenu.setCurrentIndex(1)
        elif self.ui.iconAlimento.isChecked() or self.ui.fullAlimento.isChecked():
            self.ui.multipleMenu.setCurrentIndex(2)
        elif self.ui.iconClientes.isChecked() or self.ui.fullCliente.isChecked():
            self.ui.multipleMenu.setCurrentIndex(3)
            self.showCustomers()
        elif self.ui.iconEmpleados.isChecked() or self.ui.fullEmpleado.isChecked():
            self.ui.multipleMenu.setCurrentIndex(4)
        elif self.ui.iconProveedor.isChecked() or self.ui.fullProveedor.isChecked():
            self.ui.multipleMenu.setCurrentIndex(5)
            
    @Slot()
    def addClienteWindow(self):
        if self.ui.IconWidget.isVisible():
            self.icon = True
        elif self.ui.FullWidget.isVisible():
            self.icon = False
            
        self.ui.IconWidget.setVisible(False)
        self.ui.FullWidget.setVisible(False)
        self.ui.multipleMenu.setCurrentIndex(7)
        
        nextFree = 0
        i = 1
        for cliente in self.customers:
            if(int(cliente.getID()) == i):
                nextFree = int(cliente.getID())+1
            i += 1
            
        self.ui.ID_cliente.setText(str(nextFree))
        
    @Slot()
    def modifyClienteWindow(self):
        if self.ui.IconWidget.isVisible():
            self.icon = True
        elif self.ui.FullWidget.isVisible():
            self.icon = False
            
        self.ui.IconWidget.setVisible(False)
        self.ui.FullWidget.setVisible(False)
        self.ui.multipleMenu.setCurrentIndex(8)
        
        customer = self.customers[self.customerRow]
                
        self.ui.ID_cliente_2.setText(customer.getID())
        self.ui.nameCliente_2.setText(customer.getName())
        self.ui.RFCCliente_2.setText(customer.getRFC())
        self.ui.phoneCliente_2.setText(customer.getPhoneNumber())
        self.ui.mailCliente_2.setText(customer.getMail())
        
    @Slot()
    def deleteClienteWindow(self):
        if self.ui.IconWidget.isVisible():
            self.icon = True
        elif self.ui.FullWidget.isVisible():
            self.icon = False
            
        self.ui.IconWidget.setVisible(False)
        self.ui.FullWidget.setVisible(False)
        self.ui.multipleMenu.setCurrentIndex(9)
        
        customer = self.customers[self.customerRow]
                
        self.ui.ID_cliente_3.setText(customer.getID())
        self.ui.nameCliente_3.setText(customer.getName())
        self.ui.RFCCliente_3.setText(customer.getRFC())
        self.ui.phoneCliente_3.setText(customer.getPhoneNumber())
        self.ui.mailCliente_3.setText(customer.getMail())
        
    @Slot()
    def cancelClienteWindow(self):
        if self.icon:
            self.ui.IconWidget.setVisible(True)
        else:
            self.ui.FullWidget.setVisible(True)
        self.ui.multipleMenu.setCurrentIndex(3)
        
        self.ui.nameCliente.setText("")
        self.ui.RFCCliente.setText("")
        self.ui.phoneCliente.setText("")
        self.ui.mailCliente.setText("")
        
    @Slot()
    def searchClienteWindow(self):
        self.ui.ID_busqueda_label.setVisible(True)
        self.ui.buscarEmpleado_linea.setVisible(True)
        self.ui.busquedaClienteConfirm.setVisible(True)
        
    @Slot()
    def clearBusquedaCliente(self):
        self.ui.buscarEmpleado_linea.setText("")
        self.ui.buscarEmpleado_linea.setVisible(False)
        self.ui.busquedaClienteConfirm.setVisible(False)
        self.ui.ID_busqueda_label.setVisible(False)
        
        self.ui.tablaClientes.clear()
        self.showCustomers()
        
    @Slot()
    def saveCliente(self):
        id = self.ui.ID_cliente.text()
        name = self.ui.nameCliente.text()
        rfc = self.ui.RFCCliente.text()
        phone = self.ui.phoneCliente.text()
        mail = self.ui.mailCliente.text()
        
        customer = Client(id,name,rfc,phone,mail)
        self.customers.append(customer)
        
        self.cancelClienteWindow()
        self.showCustomers()
        self.writeCustomer()
        
        self.ui.nameCliente.setText("")
        self.ui.RFCCliente.setText("")
        self.ui.phoneCliente.setText("")
        self.ui.mailCliente.setText("")
            
    @Slot()
    def modifyCliente(self):
        id = self.ui.ID_cliente_2.text()
        name = self.ui.nameCliente_2.text()
        rfc = self.ui.RFCCliente_2.text()
        phone = self.ui.phoneCliente_2.text()
        mail = self.ui.mailCliente_2.text()
        
        customer = Client(id,name,rfc,phone,mail)
        self.customers[self.customerRow] = customer
        
        self.cancelClienteWindow()
        self.showCustomers()
        self.writeCustomer()
        
    @Slot()
    def deleteClient(self):
        customer = self.customers[self.customerRow]
        self.customers.remove(customer)
        
        self.cancelClienteWindow()
        self.showCustomers()
        self.writeCustomer()
        
    @Slot()
    def searchCliente(self):
        search_id = self.ui.buscarEmpleado_linea.text()
        encontrado = False
        
        for cliente in self.customers:
            if cliente.getID() == search_id:
                encontrado = True
                resultado = cliente
                
        if encontrado:
            self.ui.tablaClientes.clear()
            self.ui.tablaClientes.setColumnCount(5)
            headers = ["ID","Nombre del Cliente","RFC","Teléfono","Correo Electrónico"]
            self.ui.tablaClientes.setHorizontalHeaderLabels(headers)
            self.ui.tablaClientes.verticalHeader().setVisible(False)
            
            self.ui.tablaClientes.setRowCount(1)
            
            self.ui.tablaClientes.setColumnWidth(0, 10)
            self.ui.tablaClientes.setColumnWidth(1, 300)
            self.ui.tablaClientes.setColumnWidth(2, 120)
            self.ui.tablaClientes.setColumnWidth(3, 120)
            self.ui.tablaClientes.setColumnWidth(4, 250)
            
            id = QTableWidgetItem(resultado.getID())
            name = QTableWidgetItem(resultado.getName())
            rfc = QTableWidgetItem(resultado.getRFC())
            phone = QTableWidgetItem(resultado.getPhoneNumber())
            mail = QTableWidgetItem(resultado.getMail())
            
            self.ui.tablaClientes.setItem(0,0,id)
            self.ui.tablaClientes.setItem(0,1,name)
            self.ui.tablaClientes.setItem(0,2,rfc)
            self.ui.tablaClientes.setItem(0,3,phone)
            self.ui.tablaClientes.setItem(0,4,mail)
        else:
            QMessageBox.information(
                self,
            "Error",
            "No hay ningun cliente con el ID " + search_id + "."
            )
                
        
    def writeCustomer(self):
        dir_path = os.path.dirname(__file__)
        file_path = os.path.join(dir_path, "customers.json")
        
        with open(file_path, "w") as file:
            data = [objeto.toDict() for objeto in self.customers]
            json.dump(data, file,indent=5)
        
    @Slot()
    def releaseSaveCliente(self):
        if self.ui.nameCliente.text() and self.ui.RFCCliente.text() and self.ui.phoneCliente.text() and self.ui.mailCliente.text():
            self.ui.saveCliente.setEnabled(True)
        else:
            self.ui.saveCliente.setEnabled(False)
    
    @Slot()
    def selectionOfCustomer(self):
        selected_items = self.ui.tablaClientes.selectedItems()
         
        if selected_items:
            for item in selected_items:
                self.customerRow = item.row()
                self.currentSelection = item.text()
                
        print(f"Elemento seleccionado: {item.text()} (Fila: {self.customerRow})")
            
    def showCustomers(self):
        self.ui.tablaClientes.setColumnCount(5)
        headers = ["ID","Nombre del Cliente","RFC","Teléfono","Correo Electrónico"]
        self.ui.tablaClientes.setHorizontalHeaderLabels(headers)
        self.ui.tablaClientes.verticalHeader().setVisible(False)
        
        self.ui.tablaClientes.setRowCount(len(self.customers))
        
        self.ui.tablaClientes.setColumnWidth(0, 10)
        self.ui.tablaClientes.setColumnWidth(1, 300)
        self.ui.tablaClientes.setColumnWidth(2, 120)
        self.ui.tablaClientes.setColumnWidth(3, 120)
        self.ui.tablaClientes.setColumnWidth(4, 250)
        
        row = 0
        for cliente in self.customers:
            id = QTableWidgetItem(cliente.getID())
            name = QTableWidgetItem(cliente.getName())
            rfc = QTableWidgetItem(cliente.getRFC())
            phone = QTableWidgetItem(cliente.getPhoneNumber())
            mail = QTableWidgetItem(cliente.getMail())
            
            self.ui.tablaClientes.setItem(row,0,id)
            self.ui.tablaClientes.setItem(row,1,name)
            self.ui.tablaClientes.setItem(row,2,rfc)
            self.ui.tablaClientes.setItem(row,3,phone)
            self.ui.tablaClientes.setItem(row,4,mail)
        
            row += 1