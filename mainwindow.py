from PySide2.QtWidgets import QMainWindow, QApplication, QToolTip
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("FastFast")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.FullWidget.setVisible(False)
        self.ui.iconHome.clicked.connect(self.button_logic)
        self.ui.fullHome.clicked.connect(self.button_logic)
        
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
        
        self.ui.multipleMenu.setCurrentIndex(6)

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
        elif self.ui.iconEmpleados.isChecked() or self.ui.fullEmpleado.isChecked():
            self.ui.multipleMenu.setCurrentIndex(4)
        elif self.ui.iconProveedor.isChecked() or self.ui.fullProveedor.isChecked():
            self.ui.multipleMenu.setCurrentIndex(5)