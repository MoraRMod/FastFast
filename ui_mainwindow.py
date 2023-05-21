# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 621)
        icon = QIcon()
        icon.addFile(u":/icons/icon/logoIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(50, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.IconWidget = QWidget(self.centralwidget)
        self.IconWidget.setObjectName(u"IconWidget")
        self.IconWidget.setStyleSheet(u"background-color: #313a46; width:50px;")
        self.verticalLayout_3 = QVBoxLayout(self.IconWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.iconHome = QPushButton(self.IconWidget)
        self.iconHome.setObjectName(u"iconHome")
        self.iconHome.setMinimumSize(QSize(70, 60))
        self.iconHome.setMaximumSize(QSize(70, 60))
        self.iconHome.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	padding: 5px;\n"
"	width: 30px;\n"
"	height: 50px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/fastfast.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.iconHome.setIcon(icon1)
        self.iconHome.setIconSize(QSize(60, 60))
        self.iconHome.setCheckable(True)
        self.iconHome.setAutoExclusive(False)
        self.iconHome.setAutoRepeatDelay(0)
        self.iconHome.setAutoRepeatInterval(0)

        self.verticalLayout_3.addWidget(self.iconHome)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.iconFactura = QPushButton(self.IconWidget)
        self.iconFactura.setObjectName(u"iconFactura")
        self.iconFactura.setStyleSheet(u"QPushButton {\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/bill.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icon/bill_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconFactura.setIcon(icon2)
        self.iconFactura.setIconSize(QSize(30, 30))
        self.iconFactura.setCheckable(True)
        self.iconFactura.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconFactura)

        self.iconPedido = QPushButton(self.IconWidget)
        self.iconPedido.setObjectName(u"iconPedido")
        self.iconPedido.setStyleSheet(u"QPushButton {\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/ticket.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icon/ticket_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconPedido.setIcon(icon3)
        self.iconPedido.setIconSize(QSize(30, 30))
        self.iconPedido.setCheckable(True)
        self.iconPedido.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconPedido)

        self.iconAlimento = QPushButton(self.IconWidget)
        self.iconAlimento.setObjectName(u"iconAlimento")
        self.iconAlimento.setStyleSheet(u"QPushButton {\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/products.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icon/products_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconAlimento.setIcon(icon4)
        self.iconAlimento.setIconSize(QSize(30, 30))
        self.iconAlimento.setCheckable(True)
        self.iconAlimento.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconAlimento)

        self.iconClientes = QPushButton(self.IconWidget)
        self.iconClientes.setObjectName(u"iconClientes")
        self.iconClientes.setStyleSheet(u"QPushButton {\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/customer.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/icon/customer_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconClientes.setIcon(icon5)
        self.iconClientes.setIconSize(QSize(30, 30))
        self.iconClientes.setCheckable(True)
        self.iconClientes.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconClientes)

        self.iconEmpleados = QPushButton(self.IconWidget)
        self.iconEmpleados.setObjectName(u"iconEmpleados")
        self.iconEmpleados.setStyleSheet(u"QPushButton {\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/employee.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/icon/employee_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconEmpleados.setIcon(icon6)
        self.iconEmpleados.setIconSize(QSize(30, 30))
        self.iconEmpleados.setCheckable(True)
        self.iconEmpleados.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconEmpleados)

        self.iconProveedor = QPushButton(self.IconWidget)
        self.iconProveedor.setObjectName(u"iconProveedor")
        self.iconProveedor.setStyleSheet(u"QPushButton {\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/supplier.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u":/icons/icon/supplier_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconProveedor.setIcon(icon7)
        self.iconProveedor.setIconSize(QSize(30, 30))
        self.iconProveedor.setCheckable(True)
        self.iconProveedor.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.iconProveedor)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 249, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.IconWidget)

        self.FullWidget = QWidget(self.centralwidget)
        self.FullWidget.setObjectName(u"FullWidget")
        self.FullWidget.setStyleSheet(u"background-color: #313a46;")
        self.gridLayout_3 = QGridLayout(self.FullWidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.fullFactura = QPushButton(self.FullWidget)
        self.fullFactura.setObjectName(u"fullFactura")
        self.fullFactura.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(9)
        self.fullFactura.setFont(font)
        self.fullFactura.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"	text-align: left;\n"
"	pading 8px 0 8px 15px;\n"
"	color: rgb(120, 133, 150);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: #fff;\n"
"}\n"
"")
        self.fullFactura.setIcon(icon2)
        self.fullFactura.setIconSize(QSize(20, 20))
        self.fullFactura.setCheckable(True)
        self.fullFactura.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullFactura)

        self.fullPedido = QPushButton(self.FullWidget)
        self.fullPedido.setObjectName(u"fullPedido")
        self.fullPedido.setMinimumSize(QSize(0, 30))
        self.fullPedido.setFont(font)
        self.fullPedido.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"	text-align: left;\n"
"	pading 8px 0 8px 15px;\n"
"	color: rgb(120, 133, 150);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: #fff;\n"
"}\n"
"")
        self.fullPedido.setIcon(icon3)
        self.fullPedido.setIconSize(QSize(20, 20))
        self.fullPedido.setCheckable(True)
        self.fullPedido.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullPedido)

        self.fullAlimento = QPushButton(self.FullWidget)
        self.fullAlimento.setObjectName(u"fullAlimento")
        self.fullAlimento.setMinimumSize(QSize(0, 30))
        self.fullAlimento.setFont(font)
        self.fullAlimento.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"	text-align: left;\n"
"	pading 8px 0 8px 15px;\n"
"	color: rgb(120, 133, 150);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: #fff;\n"
"}\n"
"")
        self.fullAlimento.setIcon(icon4)
        self.fullAlimento.setIconSize(QSize(20, 20))
        self.fullAlimento.setCheckable(True)
        self.fullAlimento.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullAlimento)

        self.fullCliente = QPushButton(self.FullWidget)
        self.fullCliente.setObjectName(u"fullCliente")
        self.fullCliente.setMinimumSize(QSize(0, 30))
        self.fullCliente.setFont(font)
        self.fullCliente.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"	text-align: left;\n"
"	pading 8px 0 8px 15px;\n"
"	color: rgb(120, 133, 150);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: #fff;\n"
"}\n"
"")
        self.fullCliente.setIcon(icon5)
        self.fullCliente.setIconSize(QSize(20, 20))
        self.fullCliente.setCheckable(True)
        self.fullCliente.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullCliente)

        self.fullEmpleado = QPushButton(self.FullWidget)
        self.fullEmpleado.setObjectName(u"fullEmpleado")
        self.fullEmpleado.setMinimumSize(QSize(0, 30))
        self.fullEmpleado.setFont(font)
        self.fullEmpleado.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"	text-align: left;\n"
"	pading 8px 0 8px 15px;\n"
"	color: rgb(120, 133, 150);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: #fff;\n"
"}\n"
"")
        self.fullEmpleado.setIcon(icon6)
        self.fullEmpleado.setIconSize(QSize(20, 20))
        self.fullEmpleado.setCheckable(True)
        self.fullEmpleado.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullEmpleado)

        self.fullProveedor = QPushButton(self.FullWidget)
        self.fullProveedor.setObjectName(u"fullProveedor")
        self.fullProveedor.setMinimumSize(QSize(105, 30))
        self.fullProveedor.setFont(font)
        self.fullProveedor.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"	border-radius: 3px;\n"
"	text-align: left;\n"
"	pading 8px 0 8px 15px;\n"
"	color: rgb(120, 133, 150);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	color: #fff;\n"
"}\n"
"")
        self.fullProveedor.setIcon(icon7)
        self.fullProveedor.setIconSize(QSize(20, 20))
        self.fullProveedor.setCheckable(True)
        self.fullProveedor.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fullProveedor)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.fullHome = QPushButton(self.FullWidget)
        self.fullHome.setObjectName(u"fullHome")
        self.fullHome.setMinimumSize(QSize(50, 60))
        self.fullHome.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setPointSize(15)
        self.fullHome.setFont(font1)
        self.fullHome.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	padding: 5px;\n"
"	width: 30px;\n"
"	height: 50px;\n"
"}")
        self.fullHome.setIcon(icon1)
        self.fullHome.setIconSize(QSize(60, 60))
        self.fullHome.setCheckable(True)
        self.fullHome.setAutoExclusive(False)
        self.fullHome.setAutoRepeatDelay(0)
        self.fullHome.setAutoRepeatInterval(0)

        self.gridLayout_3.addWidget(self.fullHome, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 379, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.FullWidget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.multipleMenu = QStackedWidget(self.widget_3)
        self.multipleMenu.setObjectName(u"multipleMenu")
        self.pageFacturas = QWidget()
        self.pageFacturas.setObjectName(u"pageFacturas")
        self.gridLayout_2 = QGridLayout(self.pageFacturas)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tablaFacturas = QTableView(self.pageFacturas)
        self.tablaFacturas.setObjectName(u"tablaFacturas")
        self.tablaFacturas.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.tablaFacturas, 1, 0, 1, 1)

        self.facturaWidget = QWidget(self.pageFacturas)
        self.facturaWidget.setObjectName(u"facturaWidget")
        self.facturaWidget.setMinimumSize(QSize(0, 58))
        self.facturaWidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.facturaWidget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.addFactura = QPushButton(self.facturaWidget)
        self.addFactura.setObjectName(u"addFactura")
        self.addFactura.setMinimumSize(QSize(40, 40))
        self.addFactura.setAutoFillBackground(False)
        self.addFactura.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.addFactura.setIcon(icon8)
        self.addFactura.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.addFactura)

        self.modifyFactura = QPushButton(self.facturaWidget)
        self.modifyFactura.setObjectName(u"modifyFactura")
        self.modifyFactura.setEnabled(False)
        self.modifyFactura.setMinimumSize(QSize(40, 40))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/modify.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/icon/modifyOff.ico", QSize(), QIcon.Disabled, QIcon.Off)
        self.modifyFactura.setIcon(icon9)
        self.modifyFactura.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.modifyFactura)

        self.deleteFactura = QPushButton(self.facturaWidget)
        self.deleteFactura.setObjectName(u"deleteFactura")
        self.deleteFactura.setEnabled(False)
        self.deleteFactura.setMinimumSize(QSize(40, 40))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icon/cancel.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u":/icons/icon/cancelOff.ico", QSize(), QIcon.Disabled, QIcon.Off)
        self.deleteFactura.setIcon(icon10)
        self.deleteFactura.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.deleteFactura)

        self.line = QFrame(self.facturaWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.searchFactura = QPushButton(self.facturaWidget)
        self.searchFactura.setObjectName(u"searchFactura")
        self.searchFactura.setMinimumSize(QSize(40, 40))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icon/search.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.searchFactura.setIcon(icon11)
        self.searchFactura.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.searchFactura)

        self.cleanFactura = QPushButton(self.facturaWidget)
        self.cleanFactura.setObjectName(u"cleanFactura")
        self.cleanFactura.setMinimumSize(QSize(40, 40))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icon/reload.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cleanFactura.setIcon(icon12)
        self.cleanFactura.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.cleanFactura)

        self.horizontalSpacer_2 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addWidget(self.facturaWidget, 0, 0, 1, 1)

        self.multipleMenu.addWidget(self.pageFacturas)
        self.pagePedidos = QWidget()
        self.pagePedidos.setObjectName(u"pagePedidos")
        self.gridLayout_4 = QGridLayout(self.pagePedidos)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pedidoWidget = QWidget(self.pagePedidos)
        self.pedidoWidget.setObjectName(u"pedidoWidget")
        self.pedidoWidget.setMinimumSize(QSize(0, 58))
        self.pedidoWidget.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.pedidoWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addPedido = QPushButton(self.pedidoWidget)
        self.addPedido.setObjectName(u"addPedido")
        self.addPedido.setMinimumSize(QSize(40, 40))
        self.addPedido.setAutoFillBackground(False)
        self.addPedido.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        self.addPedido.setIcon(icon8)
        self.addPedido.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.addPedido)

        self.modifyPedido = QPushButton(self.pedidoWidget)
        self.modifyPedido.setObjectName(u"modifyPedido")
        self.modifyPedido.setMinimumSize(QSize(40, 40))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icon/modify.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.modifyPedido.setIcon(icon13)
        self.modifyPedido.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.modifyPedido)

        self.deletePedido = QPushButton(self.pedidoWidget)
        self.deletePedido.setObjectName(u"deletePedido")
        self.deletePedido.setMinimumSize(QSize(40, 40))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icon/cancel.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.deletePedido.setIcon(icon14)
        self.deletePedido.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.deletePedido)

        self.line_3 = QFrame(self.pedidoWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.searchPedido = QPushButton(self.pedidoWidget)
        self.searchPedido.setObjectName(u"searchPedido")
        self.searchPedido.setMinimumSize(QSize(40, 40))
        self.searchPedido.setIcon(icon11)
        self.searchPedido.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.searchPedido)

        self.cleanPedido = QPushButton(self.pedidoWidget)
        self.cleanPedido.setObjectName(u"cleanPedido")
        self.cleanPedido.setMinimumSize(QSize(40, 40))
        self.cleanPedido.setIcon(icon12)
        self.cleanPedido.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.cleanPedido)

        self.horizontalSpacer_3 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_4.addWidget(self.pedidoWidget, 0, 0, 1, 1)

        self.tablaPedidos = QTableView(self.pagePedidos)
        self.tablaPedidos.setObjectName(u"tablaPedidos")
        self.tablaPedidos.setMinimumSize(QSize(0, 480))

        self.gridLayout_4.addWidget(self.tablaPedidos, 1, 0, 1, 1)

        self.multipleMenu.addWidget(self.pagePedidos)
        self.pageAlimentos = QWidget()
        self.pageAlimentos.setObjectName(u"pageAlimentos")
        self.gridLayout_5 = QGridLayout(self.pageAlimentos)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.alimentosWidget = QWidget(self.pageAlimentos)
        self.alimentosWidget.setObjectName(u"alimentosWidget")
        self.alimentosWidget.setMinimumSize(QSize(0, 58))
        self.alimentosWidget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.alimentosWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.addAlimento = QPushButton(self.alimentosWidget)
        self.addAlimento.setObjectName(u"addAlimento")
        self.addAlimento.setMinimumSize(QSize(40, 40))
        self.addAlimento.setAutoFillBackground(False)
        self.addAlimento.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        self.addAlimento.setIcon(icon8)
        self.addAlimento.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.addAlimento)

        self.modifyAlimento = QPushButton(self.alimentosWidget)
        self.modifyAlimento.setObjectName(u"modifyAlimento")
        self.modifyAlimento.setMinimumSize(QSize(40, 40))
        self.modifyAlimento.setIcon(icon13)
        self.modifyAlimento.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.modifyAlimento)

        self.deleteAlimento = QPushButton(self.alimentosWidget)
        self.deleteAlimento.setObjectName(u"deleteAlimento")
        self.deleteAlimento.setMinimumSize(QSize(40, 40))
        self.deleteAlimento.setIcon(icon14)
        self.deleteAlimento.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.deleteAlimento)

        self.line_4 = QFrame(self.alimentosWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.searchAlimento = QPushButton(self.alimentosWidget)
        self.searchAlimento.setObjectName(u"searchAlimento")
        self.searchAlimento.setMinimumSize(QSize(40, 40))
        self.searchAlimento.setIcon(icon11)
        self.searchAlimento.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.searchAlimento)

        self.cleanAlimento = QPushButton(self.alimentosWidget)
        self.cleanAlimento.setObjectName(u"cleanAlimento")
        self.cleanAlimento.setMinimumSize(QSize(40, 40))
        self.cleanAlimento.setIcon(icon12)
        self.cleanAlimento.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.cleanAlimento)

        self.horizontalSpacer_4 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.gridLayout_5.addWidget(self.alimentosWidget, 0, 0, 1, 1)

        self.tablaAlimentos = QTableView(self.pageAlimentos)
        self.tablaAlimentos.setObjectName(u"tablaAlimentos")

        self.gridLayout_5.addWidget(self.tablaAlimentos, 1, 0, 1, 1)

        self.multipleMenu.addWidget(self.pageAlimentos)
        self.pageClientes = QWidget()
        self.pageClientes.setObjectName(u"pageClientes")
        self.gridLayout_6 = QGridLayout(self.pageClientes)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.clientesWidget = QWidget(self.pageClientes)
        self.clientesWidget.setObjectName(u"clientesWidget")
        self.clientesWidget.setMinimumSize(QSize(0, 58))
        self.clientesWidget.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.clientesWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.addCliente = QPushButton(self.clientesWidget)
        self.addCliente.setObjectName(u"addCliente")
        self.addCliente.setMinimumSize(QSize(40, 40))
        self.addCliente.setAutoFillBackground(False)
        self.addCliente.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        self.addCliente.setIcon(icon8)
        self.addCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.addCliente)

        self.modifyCliente = QPushButton(self.clientesWidget)
        self.modifyCliente.setObjectName(u"modifyCliente")
        self.modifyCliente.setMinimumSize(QSize(40, 40))
        self.modifyCliente.setIcon(icon13)
        self.modifyCliente.setIconSize(QSize(28, 28))

        self.horizontalLayout_5.addWidget(self.modifyCliente)

        self.deleteCliente = QPushButton(self.clientesWidget)
        self.deleteCliente.setObjectName(u"deleteCliente")
        self.deleteCliente.setMinimumSize(QSize(40, 40))
        self.deleteCliente.setIcon(icon14)
        self.deleteCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.deleteCliente)

        self.line_5 = QFrame(self.clientesWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_5)

        self.searchCliente = QPushButton(self.clientesWidget)
        self.searchCliente.setObjectName(u"searchCliente")
        self.searchCliente.setMinimumSize(QSize(40, 40))
        self.searchCliente.setIcon(icon11)
        self.searchCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.searchCliente)

        self.ID_busqueda_label = QLabel(self.clientesWidget)
        self.ID_busqueda_label.setObjectName(u"ID_busqueda_label")

        self.horizontalLayout_5.addWidget(self.ID_busqueda_label)

        self.buscarEmpleado_linea = QLineEdit(self.clientesWidget)
        self.buscarEmpleado_linea.setObjectName(u"buscarEmpleado_linea")
        self.buscarEmpleado_linea.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.buscarEmpleado_linea)

        self.busquedaClienteConfirm = QPushButton(self.clientesWidget)
        self.busquedaClienteConfirm.setObjectName(u"busquedaClienteConfirm")
        self.busquedaClienteConfirm.setIcon(icon11)

        self.horizontalLayout_5.addWidget(self.busquedaClienteConfirm)

        self.cleanCliente = QPushButton(self.clientesWidget)
        self.cleanCliente.setObjectName(u"cleanCliente")
        self.cleanCliente.setMinimumSize(QSize(40, 40))
        self.cleanCliente.setIcon(icon12)
        self.cleanCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.cleanCliente)

        self.horizontalSpacer_5 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.gridLayout_6.addWidget(self.clientesWidget, 0, 0, 1, 1)

        self.tablaClientes = QTableWidget(self.pageClientes)
        self.tablaClientes.setObjectName(u"tablaClientes")

        self.gridLayout_6.addWidget(self.tablaClientes, 1, 0, 1, 1)

        self.multipleMenu.addWidget(self.pageClientes)
        self.pageEmpleados = QWidget()
        self.pageEmpleados.setObjectName(u"pageEmpleados")
        self.gridLayout_7 = QGridLayout(self.pageEmpleados)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.empleadosWidget = QWidget(self.pageEmpleados)
        self.empleadosWidget.setObjectName(u"empleadosWidget")
        self.empleadosWidget.setMinimumSize(QSize(0, 58))
        self.empleadosWidget.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.empleadosWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.addEmpleado = QPushButton(self.empleadosWidget)
        self.addEmpleado.setObjectName(u"addEmpleado")
        self.addEmpleado.setMinimumSize(QSize(40, 40))
        self.addEmpleado.setAutoFillBackground(False)
        self.addEmpleado.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        self.addEmpleado.setIcon(icon8)
        self.addEmpleado.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.addEmpleado)

        self.modifyEmpleado = QPushButton(self.empleadosWidget)
        self.modifyEmpleado.setObjectName(u"modifyEmpleado")
        self.modifyEmpleado.setMinimumSize(QSize(40, 40))
        self.modifyEmpleado.setIcon(icon13)
        self.modifyEmpleado.setIconSize(QSize(28, 28))

        self.horizontalLayout_7.addWidget(self.modifyEmpleado)

        self.deleteEmpleado = QPushButton(self.empleadosWidget)
        self.deleteEmpleado.setObjectName(u"deleteEmpleado")
        self.deleteEmpleado.setMinimumSize(QSize(40, 40))
        self.deleteEmpleado.setIcon(icon14)
        self.deleteEmpleado.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.deleteEmpleado)

        self.line_7 = QFrame(self.empleadosWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.line_7)

        self.searchEmpleado = QPushButton(self.empleadosWidget)
        self.searchEmpleado.setObjectName(u"searchEmpleado")
        self.searchEmpleado.setMinimumSize(QSize(40, 40))
        self.searchEmpleado.setIcon(icon11)
        self.searchEmpleado.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.searchEmpleado)

        self.cleanEmpleado = QPushButton(self.empleadosWidget)
        self.cleanEmpleado.setObjectName(u"cleanEmpleado")
        self.cleanEmpleado.setMinimumSize(QSize(40, 40))
        self.cleanEmpleado.setIcon(icon12)
        self.cleanEmpleado.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.cleanEmpleado)

        self.horizontalSpacer_7 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.gridLayout_7.addWidget(self.empleadosWidget, 0, 0, 1, 1)

        self.tablaEmpleado = QTableView(self.pageEmpleados)
        self.tablaEmpleado.setObjectName(u"tablaEmpleado")

        self.gridLayout_7.addWidget(self.tablaEmpleado, 1, 0, 1, 1)

        self.multipleMenu.addWidget(self.pageEmpleados)
        self.pageProveedores = QWidget()
        self.pageProveedores.setObjectName(u"pageProveedores")
        self.gridLayout_8 = QGridLayout(self.pageProveedores)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.proveedorWidget = QWidget(self.pageProveedores)
        self.proveedorWidget.setObjectName(u"proveedorWidget")
        self.proveedorWidget.setMinimumSize(QSize(0, 58))
        self.proveedorWidget.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.proveedorWidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.addProveedor = QPushButton(self.proveedorWidget)
        self.addProveedor.setObjectName(u"addProveedor")
        self.addProveedor.setMinimumSize(QSize(40, 40))
        self.addProveedor.setAutoFillBackground(False)
        self.addProveedor.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        self.addProveedor.setIcon(icon8)
        self.addProveedor.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.addProveedor)

        self.modifyProveedor = QPushButton(self.proveedorWidget)
        self.modifyProveedor.setObjectName(u"modifyProveedor")
        self.modifyProveedor.setMinimumSize(QSize(40, 40))
        self.modifyProveedor.setIcon(icon13)
        self.modifyProveedor.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.modifyProveedor)

        self.deleteProveedor = QPushButton(self.proveedorWidget)
        self.deleteProveedor.setObjectName(u"deleteProveedor")
        self.deleteProveedor.setMinimumSize(QSize(40, 40))
        self.deleteProveedor.setIcon(icon14)
        self.deleteProveedor.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.deleteProveedor)

        self.line_8 = QFrame(self.proveedorWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_8)

        self.searchProveedor = QPushButton(self.proveedorWidget)
        self.searchProveedor.setObjectName(u"searchProveedor")
        self.searchProveedor.setMinimumSize(QSize(40, 40))
        self.searchProveedor.setIcon(icon11)
        self.searchProveedor.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.searchProveedor)

        self.cleanProveedor = QPushButton(self.proveedorWidget)
        self.cleanProveedor.setObjectName(u"cleanProveedor")
        self.cleanProveedor.setMinimumSize(QSize(40, 40))
        self.cleanProveedor.setIcon(icon12)
        self.cleanProveedor.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.cleanProveedor)

        self.horizontalSpacer_8 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.gridLayout_8.addWidget(self.proveedorWidget, 0, 0, 1, 1)

        self.tablaProveedor = QTableWidget(self.pageProveedores)
        self.tablaProveedor.setObjectName(u"tablaProveedor")

        self.gridLayout_8.addWidget(self.tablaProveedor, 1, 0, 1, 1)

        self.multipleMenu.addWidget(self.pageProveedores)
        self.defaultPage = QWidget()
        self.defaultPage.setObjectName(u"defaultPage")
        self.gridLayout_10 = QGridLayout(self.defaultPage)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.label = QLabel(self.defaultPage)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/icon/fastfast.ico"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label, 1, 0, 1, 1)

        self.label_7 = QLabel(self.defaultPage)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light Condensed")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setKerning(True)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_7, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.multipleMenu.addWidget(self.defaultPage)
        self.addCliente_page = QWidget()
        self.addCliente_page.setObjectName(u"addCliente_page")
        self.gridLayout_9 = QGridLayout(self.addCliente_page)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.proveedorWidget_2 = QWidget(self.addCliente_page)
        self.proveedorWidget_2.setObjectName(u"proveedorWidget_2")
        self.proveedorWidget_2.setMinimumSize(QSize(0, 58))
        self.proveedorWidget_2.setMaximumSize(QSize(16777215, 58))
        self.proveedorWidget_2.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.proveedorWidget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.saveCliente = QPushButton(self.proveedorWidget_2)
        self.saveCliente.setObjectName(u"saveCliente")
        self.saveCliente.setEnabled(False)
        self.saveCliente.setMinimumSize(QSize(40, 40))
        self.saveCliente.setAutoFillBackground(False)
        self.saveCliente.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icon/save.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon15.addFile(u":/icons/icon/saveOff.ico", QSize(), QIcon.Disabled, QIcon.Off)
        self.saveCliente.setIcon(icon15)
        self.saveCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.saveCliente)

        self.cancelOpCliente = QPushButton(self.proveedorWidget_2)
        self.cancelOpCliente.setObjectName(u"cancelOpCliente")
        self.cancelOpCliente.setMinimumSize(QSize(40, 40))
        icon16 = QIcon()
        icon16.addFile(u":/icons/icon/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelOpCliente.setIcon(icon16)
        self.cancelOpCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.cancelOpCliente)

        self.horizontalSpacer_9 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.label_8 = QLabel(self.proveedorWidget_2)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light Condensed")
        font3.setPointSize(15)
        self.label_8.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_8)


        self.gridLayout_9.addWidget(self.proveedorWidget_2, 0, 0, 1, 1)

        self.addCliente_Widget = QWidget(self.addCliente_page)
        self.addCliente_Widget.setObjectName(u"addCliente_Widget")
        self.addCliente_Widget.setToolTipDuration(5)
        self.addCliente_Widget.setStyleSheet(u"QWidget#addCliente_Widget{\n"
"	background-image: url(:/icons/icon/fastfast.ico);\n"
"	background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"	background-origin: content;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_11 = QGridLayout(self.addCliente_Widget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, -1, 0, -1)
        self.label_5 = QLabel(self.addCliente_Widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_11.addWidget(self.label_5, 4, 1, 1, 2)

        self.label_3 = QLabel(self.addCliente_Widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_11.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.addCliente_Widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_11.addWidget(self.label_4, 3, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_11, 2, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 427, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_6, 5, 3, 1, 1)

        self.mailCliente = QLineEdit(self.addCliente_Widget)
        self.mailCliente.setObjectName(u"mailCliente")

        self.gridLayout_11.addWidget(self.mailCliente, 4, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 427, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 5, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_12, 2, 4, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.label_6 = QLabel(self.addCliente_Widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.ID_cliente = QLineEdit(self.addCliente_Widget)
        self.ID_cliente.setObjectName(u"ID_cliente")
        self.ID_cliente.setEnabled(False)
        self.ID_cliente.setMaximumSize(QSize(50, 16777215))
        self.ID_cliente.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.ID_cliente)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.addCliente_Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.nameCliente = QLineEdit(self.addCliente_Widget)
        self.nameCliente.setObjectName(u"nameCliente")

        self.horizontalLayout_6.addWidget(self.nameCliente)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.gridLayout_11.addLayout(self.horizontalLayout_6, 0, 0, 1, 5)

        self.line_2 = QFrame(self.addCliente_Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_2, 1, 0, 1, 5)

        self.RFCCliente = QLineEdit(self.addCliente_Widget)
        self.RFCCliente.setObjectName(u"RFCCliente")

        self.gridLayout_11.addWidget(self.RFCCliente, 2, 2, 1, 2)

        self.phoneCliente = QLineEdit(self.addCliente_Widget)
        self.phoneCliente.setObjectName(u"phoneCliente")

        self.gridLayout_11.addWidget(self.phoneCliente, 3, 2, 1, 2)


        self.gridLayout_9.addWidget(self.addCliente_Widget, 1, 0, 1, 1)

        self.multipleMenu.addWidget(self.addCliente_page)
        self.modifyCliente_page = QWidget()
        self.modifyCliente_page.setObjectName(u"modifyCliente_page")
        self.gridLayout_12 = QGridLayout(self.modifyCliente_page)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.proveedorWidget_3 = QWidget(self.modifyCliente_page)
        self.proveedorWidget_3.setObjectName(u"proveedorWidget_3")
        self.proveedorWidget_3.setMinimumSize(QSize(0, 58))
        self.proveedorWidget_3.setMaximumSize(QSize(16777215, 58))
        self.proveedorWidget_3.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.proveedorWidget_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.modifyClienteConfirm = QPushButton(self.proveedorWidget_3)
        self.modifyClienteConfirm.setObjectName(u"modifyClienteConfirm")
        self.modifyClienteConfirm.setEnabled(True)
        self.modifyClienteConfirm.setMinimumSize(QSize(40, 40))
        self.modifyClienteConfirm.setAutoFillBackground(False)
        self.modifyClienteConfirm.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        self.modifyClienteConfirm.setIcon(icon13)
        self.modifyClienteConfirm.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.modifyClienteConfirm)

        self.cancelModifyCliente = QPushButton(self.proveedorWidget_3)
        self.cancelModifyCliente.setObjectName(u"cancelModifyCliente")
        self.cancelModifyCliente.setMinimumSize(QSize(40, 40))
        self.cancelModifyCliente.setIcon(icon16)
        self.cancelModifyCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.cancelModifyCliente)

        self.horizontalSpacer_18 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_18)

        self.label_15 = QLabel(self.proveedorWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_15)


        self.gridLayout_12.addWidget(self.proveedorWidget_3, 0, 0, 1, 1)

        self.modifyCliente_Widget = QWidget(self.modifyCliente_page)
        self.modifyCliente_Widget.setObjectName(u"modifyCliente_Widget")
        self.modifyCliente_Widget.setToolTipDuration(5)
        self.modifyCliente_Widget.setStyleSheet(u"QWidget#modifyCliente_Widget{\n"
"	background-image: url(:/icons/icon/fastfast.ico);\n"
"	background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"	background-origin: content;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_13 = QGridLayout(self.modifyCliente_Widget)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_15)

        self.label_12 = QLabel(self.modifyCliente_Widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.ID_cliente_2 = QLineEdit(self.modifyCliente_Widget)
        self.ID_cliente_2.setObjectName(u"ID_cliente_2")
        self.ID_cliente_2.setEnabled(False)
        self.ID_cliente_2.setMaximumSize(QSize(50, 16777215))
        self.ID_cliente_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.ID_cliente_2)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)

        self.label_13 = QLabel(self.modifyCliente_Widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)

        self.nameCliente_2 = QLineEdit(self.modifyCliente_Widget)
        self.nameCliente_2.setObjectName(u"nameCliente_2")

        self.horizontalLayout_10.addWidget(self.nameCliente_2)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_17)


        self.gridLayout_13.addLayout(self.horizontalLayout_10, 0, 0, 1, 6)

        self.phoneCliente_2 = QLineEdit(self.modifyCliente_Widget)
        self.phoneCliente_2.setObjectName(u"phoneCliente_2")

        self.gridLayout_13.addWidget(self.phoneCliente_2, 3, 3, 1, 2)

        self.label_10 = QLabel(self.modifyCliente_Widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 2, 1, 1, 2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_14, 2, 5, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 427, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 5, 1, 1, 1)

        self.mailCliente_2 = QLineEdit(self.modifyCliente_Widget)
        self.mailCliente_2.setObjectName(u"mailCliente_2")

        self.gridLayout_13.addWidget(self.mailCliente_2, 4, 4, 1, 1)

        self.label_11 = QLabel(self.modifyCliente_Widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_13.addWidget(self.label_11, 3, 1, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 427, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_7, 5, 4, 1, 1)

        self.line_6 = QFrame(self.modifyCliente_Widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_13.addWidget(self.line_6, 1, 0, 1, 6)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_13, 2, 0, 1, 1)

        self.label_9 = QLabel(self.modifyCliente_Widget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 4, 1, 1, 3)

        self.RFCCliente_2 = QLineEdit(self.modifyCliente_Widget)
        self.RFCCliente_2.setObjectName(u"RFCCliente_2")

        self.gridLayout_13.addWidget(self.RFCCliente_2, 2, 3, 1, 2)


        self.gridLayout_12.addWidget(self.modifyCliente_Widget, 2, 0, 1, 1)

        self.multipleMenu.addWidget(self.modifyCliente_page)
        self.deleteClientePage = QWidget()
        self.deleteClientePage.setObjectName(u"deleteClientePage")
        self.gridLayout_15 = QGridLayout(self.deleteClientePage)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.proveedorWidget_4 = QWidget(self.deleteClientePage)
        self.proveedorWidget_4.setObjectName(u"proveedorWidget_4")
        self.proveedorWidget_4.setMinimumSize(QSize(0, 58))
        self.proveedorWidget_4.setMaximumSize(QSize(16777215, 58))
        self.proveedorWidget_4.setStyleSheet(u"")
        self.horizontalLayout_12 = QHBoxLayout(self.proveedorWidget_4)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.deleteClienteConfirm = QPushButton(self.proveedorWidget_4)
        self.deleteClienteConfirm.setObjectName(u"deleteClienteConfirm")
        self.deleteClienteConfirm.setEnabled(True)
        self.deleteClienteConfirm.setMinimumSize(QSize(40, 40))
        self.deleteClienteConfirm.setAutoFillBackground(False)
        self.deleteClienteConfirm.setStyleSheet(u"QPushButton {\n"
"	pading 8px 0 8px 15px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icon/delete.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteClienteConfirm.setIcon(icon17)
        self.deleteClienteConfirm.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.deleteClienteConfirm)

        self.cancelDeleteCliente = QPushButton(self.proveedorWidget_4)
        self.cancelDeleteCliente.setObjectName(u"cancelDeleteCliente")
        self.cancelDeleteCliente.setMinimumSize(QSize(40, 40))
        self.cancelDeleteCliente.setIcon(icon16)
        self.cancelDeleteCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.cancelDeleteCliente)

        self.horizontalSpacer_19 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)

        self.label_16 = QLabel(self.proveedorWidget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_16)


        self.gridLayout_15.addWidget(self.proveedorWidget_4, 0, 0, 1, 1)

        self.deleteCliente_Widget = QWidget(self.deleteClientePage)
        self.deleteCliente_Widget.setObjectName(u"deleteCliente_Widget")
        self.deleteCliente_Widget.setToolTipDuration(5)
        self.deleteCliente_Widget.setStyleSheet(u"QWidget#deleteCliente_Widget{\n"
"	background-image: url(:/icons/icon/fastfast.ico);\n"
"	background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"	background-origin: content;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_14 = QGridLayout(self.deleteCliente_Widget)
        self.gridLayout_14.setSpacing(6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_22)

        self.label_17 = QLabel(self.deleteCliente_Widget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.ID_cliente_3 = QLineEdit(self.deleteCliente_Widget)
        self.ID_cliente_3.setObjectName(u"ID_cliente_3")
        self.ID_cliente_3.setEnabled(False)
        self.ID_cliente_3.setMaximumSize(QSize(50, 16777215))
        self.ID_cliente_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.ID_cliente_3)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_23)

        self.label_18 = QLabel(self.deleteCliente_Widget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.nameCliente_3 = QLineEdit(self.deleteCliente_Widget)
        self.nameCliente_3.setObjectName(u"nameCliente_3")
        self.nameCliente_3.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.nameCliente_3)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_24)


        self.gridLayout_14.addLayout(self.horizontalLayout_13, 0, 0, 1, 6)

        self.phoneCliente_3 = QLineEdit(self.deleteCliente_Widget)
        self.phoneCliente_3.setObjectName(u"phoneCliente_3")
        self.phoneCliente_3.setEnabled(False)

        self.gridLayout_14.addWidget(self.phoneCliente_3, 3, 3, 1, 2)

        self.label_19 = QLabel(self.deleteCliente_Widget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_14.addWidget(self.label_19, 2, 1, 1, 2)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_25, 2, 5, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 427, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_9, 5, 1, 1, 1)

        self.mailCliente_3 = QLineEdit(self.deleteCliente_Widget)
        self.mailCliente_3.setObjectName(u"mailCliente_3")
        self.mailCliente_3.setEnabled(False)

        self.gridLayout_14.addWidget(self.mailCliente_3, 4, 4, 1, 1)

        self.label_20 = QLabel(self.deleteCliente_Widget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_14.addWidget(self.label_20, 3, 1, 1, 2)

        self.verticalSpacer_10 = QSpacerItem(20, 427, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_10, 5, 4, 1, 1)

        self.line_9 = QFrame(self.deleteCliente_Widget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line_9, 1, 0, 1, 6)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_26, 2, 0, 1, 1)

        self.label_21 = QLabel(self.deleteCliente_Widget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_14.addWidget(self.label_21, 4, 1, 1, 3)

        self.RFCCliente_3 = QLineEdit(self.deleteCliente_Widget)
        self.RFCCliente_3.setObjectName(u"RFCCliente_3")
        self.RFCCliente_3.setEnabled(False)

        self.gridLayout_14.addWidget(self.RFCCliente_3, 2, 3, 1, 2)


        self.gridLayout_15.addWidget(self.deleteCliente_Widget, 1, 0, 1, 1)

        self.multipleMenu.addWidget(self.deleteClientePage)

        self.gridLayout.addWidget(self.multipleMenu, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.addFactura, self.modifyFactura)
        QWidget.setTabOrder(self.modifyFactura, self.deleteFactura)
        QWidget.setTabOrder(self.deleteFactura, self.searchFactura)
        QWidget.setTabOrder(self.searchFactura, self.cleanFactura)
        QWidget.setTabOrder(self.cleanFactura, self.tablaFacturas)
        QWidget.setTabOrder(self.tablaFacturas, self.addPedido)
        QWidget.setTabOrder(self.addPedido, self.modifyPedido)
        QWidget.setTabOrder(self.modifyPedido, self.deletePedido)
        QWidget.setTabOrder(self.deletePedido, self.searchPedido)
        QWidget.setTabOrder(self.searchPedido, self.cleanPedido)
        QWidget.setTabOrder(self.cleanPedido, self.tablaPedidos)
        QWidget.setTabOrder(self.tablaPedidos, self.addAlimento)
        QWidget.setTabOrder(self.addAlimento, self.modifyAlimento)
        QWidget.setTabOrder(self.modifyAlimento, self.deleteAlimento)
        QWidget.setTabOrder(self.deleteAlimento, self.searchAlimento)
        QWidget.setTabOrder(self.searchAlimento, self.cleanAlimento)
        QWidget.setTabOrder(self.cleanAlimento, self.tablaAlimentos)
        QWidget.setTabOrder(self.tablaAlimentos, self.addCliente)
        QWidget.setTabOrder(self.addCliente, self.modifyCliente)
        QWidget.setTabOrder(self.modifyCliente, self.deleteCliente)
        QWidget.setTabOrder(self.deleteCliente, self.searchCliente)
        QWidget.setTabOrder(self.searchCliente, self.cleanCliente)
        QWidget.setTabOrder(self.cleanCliente, self.tablaClientes)
        QWidget.setTabOrder(self.tablaClientes, self.addEmpleado)
        QWidget.setTabOrder(self.addEmpleado, self.modifyEmpleado)
        QWidget.setTabOrder(self.modifyEmpleado, self.deleteEmpleado)
        QWidget.setTabOrder(self.deleteEmpleado, self.searchEmpleado)
        QWidget.setTabOrder(self.searchEmpleado, self.cleanEmpleado)
        QWidget.setTabOrder(self.cleanEmpleado, self.tablaEmpleado)
        QWidget.setTabOrder(self.tablaEmpleado, self.addProveedor)
        QWidget.setTabOrder(self.addProveedor, self.modifyProveedor)
        QWidget.setTabOrder(self.modifyProveedor, self.deleteProveedor)
        QWidget.setTabOrder(self.deleteProveedor, self.searchProveedor)
        QWidget.setTabOrder(self.searchProveedor, self.cleanProveedor)
        QWidget.setTabOrder(self.cleanProveedor, self.tablaProveedor)
        QWidget.setTabOrder(self.tablaProveedor, self.ID_cliente)
        QWidget.setTabOrder(self.ID_cliente, self.nameCliente)
        QWidget.setTabOrder(self.nameCliente, self.RFCCliente)
        QWidget.setTabOrder(self.RFCCliente, self.phoneCliente)
        QWidget.setTabOrder(self.phoneCliente, self.mailCliente)
        QWidget.setTabOrder(self.mailCliente, self.saveCliente)
        QWidget.setTabOrder(self.saveCliente, self.cancelOpCliente)
        QWidget.setTabOrder(self.cancelOpCliente, self.iconHome)
        QWidget.setTabOrder(self.iconHome, self.fullHome)
        QWidget.setTabOrder(self.fullHome, self.iconFactura)
        QWidget.setTabOrder(self.iconFactura, self.iconPedido)
        QWidget.setTabOrder(self.iconPedido, self.iconAlimento)
        QWidget.setTabOrder(self.iconAlimento, self.iconEmpleados)
        QWidget.setTabOrder(self.iconEmpleados, self.iconProveedor)
        QWidget.setTabOrder(self.iconProveedor, self.fullProveedor)
        QWidget.setTabOrder(self.fullProveedor, self.iconClientes)
        QWidget.setTabOrder(self.iconClientes, self.fullFactura)
        QWidget.setTabOrder(self.fullFactura, self.fullPedido)
        QWidget.setTabOrder(self.fullPedido, self.fullAlimento)
        QWidget.setTabOrder(self.fullAlimento, self.fullCliente)
        QWidget.setTabOrder(self.fullCliente, self.fullEmpleado)

        self.retranslateUi(MainWindow)
        self.iconFactura.toggled.connect(self.fullFactura.setChecked)
        self.iconPedido.toggled.connect(self.fullPedido.setChecked)
        self.iconAlimento.toggled.connect(self.fullAlimento.setChecked)
        self.iconClientes.toggled.connect(self.fullCliente.setChecked)
        self.iconEmpleados.toggled.connect(self.fullEmpleado.setChecked)
        self.iconProveedor.toggled.connect(self.fullProveedor.setChecked)
        self.fullFactura.toggled.connect(self.iconFactura.setChecked)
        self.fullPedido.toggled.connect(self.iconPedido.setChecked)
        self.fullAlimento.toggled.connect(self.iconAlimento.setChecked)
        self.fullCliente.toggled.connect(self.iconClientes.setChecked)
        self.fullEmpleado.toggled.connect(self.iconEmpleados.setChecked)
        self.fullProveedor.toggled.connect(self.iconProveedor.setChecked)

        self.multipleMenu.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FastFast", None))
#if QT_CONFIG(tooltip)
        self.iconHome.setToolTip(QCoreApplication.translate("MainWindow", u"Expandir Men\u00fa.", None))
#endif // QT_CONFIG(tooltip)
        self.iconHome.setText("")
#if QT_CONFIG(tooltip)
        self.iconFactura.setToolTip(QCoreApplication.translate("MainWindow", u"Facturas", None))
#endif // QT_CONFIG(tooltip)
        self.iconFactura.setText("")
#if QT_CONFIG(tooltip)
        self.iconPedido.setToolTip(QCoreApplication.translate("MainWindow", u"Pedidos", None))
#endif // QT_CONFIG(tooltip)
        self.iconPedido.setText("")
#if QT_CONFIG(tooltip)
        self.iconAlimento.setToolTip(QCoreApplication.translate("MainWindow", u"Alimentos", None))
#endif // QT_CONFIG(tooltip)
        self.iconAlimento.setText("")
#if QT_CONFIG(tooltip)
        self.iconClientes.setToolTip(QCoreApplication.translate("MainWindow", u"Clientes", None))
#endif // QT_CONFIG(tooltip)
        self.iconClientes.setText("")
#if QT_CONFIG(tooltip)
        self.iconEmpleados.setToolTip(QCoreApplication.translate("MainWindow", u"Empleados", None))
#endif // QT_CONFIG(tooltip)
        self.iconEmpleados.setText("")
#if QT_CONFIG(tooltip)
        self.iconProveedor.setToolTip(QCoreApplication.translate("MainWindow", u"Proveedores", None))
#endif // QT_CONFIG(tooltip)
        self.iconProveedor.setText("")
        self.fullFactura.setText(QCoreApplication.translate("MainWindow", u"Facturas", None))
        self.fullPedido.setText(QCoreApplication.translate("MainWindow", u"Pedidos", None))
        self.fullAlimento.setText(QCoreApplication.translate("MainWindow", u"Alimentos", None))
        self.fullCliente.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.fullEmpleado.setText(QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.fullProveedor.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
#if QT_CONFIG(tooltip)
        self.fullHome.setToolTip(QCoreApplication.translate("MainWindow", u"Retraer Men\u00fa.", None))
#endif // QT_CONFIG(tooltip)
        self.fullHome.setText("")
#if QT_CONFIG(tooltip)
        self.addFactura.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Factura (Alt+Ins)", None))
#endif // QT_CONFIG(tooltip)
        self.addFactura.setText("")
#if QT_CONFIG(shortcut)
        self.addFactura.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Ins", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.modifyFactura.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Factura (Bloqueado)", None))
#endif // QT_CONFIG(tooltip)
        self.modifyFactura.setText("")
#if QT_CONFIG(tooltip)
        self.deleteFactura.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar Factura (Bloqueado)", None))
#endif // QT_CONFIG(tooltip)
        self.deleteFactura.setText("")
#if QT_CONFIG(tooltip)
        self.searchFactura.setToolTip(QCoreApplication.translate("MainWindow", u"Buscar Factura", None))
#endif // QT_CONFIG(tooltip)
        self.searchFactura.setText("")
#if QT_CONFIG(tooltip)
        self.cleanFactura.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar Busqueda (F6)", None))
#endif // QT_CONFIG(tooltip)
        self.cleanFactura.setText("")
#if QT_CONFIG(shortcut)
        self.cleanFactura.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.addPedido.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Pedido (Alt+Ins)", None))
#endif // QT_CONFIG(tooltip)
        self.addPedido.setText("")
#if QT_CONFIG(shortcut)
        self.addPedido.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Ins", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.modifyPedido.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Pedido", None))
#endif // QT_CONFIG(tooltip)
        self.modifyPedido.setText("")
#if QT_CONFIG(tooltip)
        self.deletePedido.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar Pedido (Alt+Supr)", None))
#endif // QT_CONFIG(tooltip)
        self.deletePedido.setText("")
#if QT_CONFIG(shortcut)
        self.deletePedido.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.searchPedido.setToolTip(QCoreApplication.translate("MainWindow", u"Buscar Pedido", None))
#endif // QT_CONFIG(tooltip)
        self.searchPedido.setText("")
#if QT_CONFIG(tooltip)
        self.cleanPedido.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar Busqueda (F6)", None))
#endif // QT_CONFIG(tooltip)
        self.cleanPedido.setText("")
#if QT_CONFIG(shortcut)
        self.cleanPedido.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.addAlimento.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Alimento (Alt+Ins)", None))
#endif // QT_CONFIG(tooltip)
        self.addAlimento.setText("")
#if QT_CONFIG(shortcut)
        self.addAlimento.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Ins", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.modifyAlimento.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Alimento", None))
#endif // QT_CONFIG(tooltip)
        self.modifyAlimento.setText("")
#if QT_CONFIG(tooltip)
        self.deleteAlimento.setToolTip(QCoreApplication.translate("MainWindow", u"Dar de baja un Alimento (Alt+Supr)", None))
#endif // QT_CONFIG(tooltip)
        self.deleteAlimento.setText("")
#if QT_CONFIG(shortcut)
        self.deleteAlimento.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.searchAlimento.setToolTip(QCoreApplication.translate("MainWindow", u"Buscar Alimento", None))
#endif // QT_CONFIG(tooltip)
        self.searchAlimento.setText("")
#if QT_CONFIG(tooltip)
        self.cleanAlimento.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar Alimento (F6)", None))
#endif // QT_CONFIG(tooltip)
        self.cleanAlimento.setText("")
#if QT_CONFIG(shortcut)
        self.cleanAlimento.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.addCliente.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Cliente (Alt+Ins)", None))
#endif // QT_CONFIG(tooltip)
        self.addCliente.setText("")
#if QT_CONFIG(shortcut)
        self.addCliente.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Ins", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.modifyCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.modifyCliente.setText("")
#if QT_CONFIG(tooltip)
        self.deleteCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Dar de baja un Cliente (Alt+Supr)", None))
#endif // QT_CONFIG(tooltip)
        self.deleteCliente.setText("")
#if QT_CONFIG(shortcut)
        self.deleteCliente.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.searchCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Buscar Cliente", None))
#endif // QT_CONFIG(tooltip)
        self.searchCliente.setText("")
        self.ID_busqueda_label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.busquedaClienteConfirm.setText("")
#if QT_CONFIG(tooltip)
        self.cleanCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar Cliente (F6)", None))
#endif // QT_CONFIG(tooltip)
        self.cleanCliente.setText("")
#if QT_CONFIG(shortcut)
        self.cleanCliente.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.addEmpleado.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Empleado (Alt+Ins)", None))
#endif // QT_CONFIG(tooltip)
        self.addEmpleado.setText("")
#if QT_CONFIG(shortcut)
        self.addEmpleado.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Ins", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.modifyEmpleado.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Empleado", None))
#endif // QT_CONFIG(tooltip)
        self.modifyEmpleado.setText("")
#if QT_CONFIG(tooltip)
        self.deleteEmpleado.setToolTip(QCoreApplication.translate("MainWindow", u"Dar de baja un Empleado (Alt+Supr)", None))
#endif // QT_CONFIG(tooltip)
        self.deleteEmpleado.setText("")
#if QT_CONFIG(shortcut)
        self.deleteEmpleado.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.searchEmpleado.setToolTip(QCoreApplication.translate("MainWindow", u"Buscar Empleado", None))
#endif // QT_CONFIG(tooltip)
        self.searchEmpleado.setText("")
#if QT_CONFIG(tooltip)
        self.cleanEmpleado.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar Busqueda (F6)", None))
#endif // QT_CONFIG(tooltip)
        self.cleanEmpleado.setText("")
#if QT_CONFIG(shortcut)
        self.cleanEmpleado.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.addProveedor.setToolTip(QCoreApplication.translate("MainWindow", u"A\u00f1adir Proveedor (Alt+Ins)", None))
#endif // QT_CONFIG(tooltip)
        self.addProveedor.setText("")
#if QT_CONFIG(shortcut)
        self.addProveedor.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Ins", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.modifyProveedor.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Proveedor", None))
#endif // QT_CONFIG(tooltip)
        self.modifyProveedor.setText("")
#if QT_CONFIG(tooltip)
        self.deleteProveedor.setToolTip(QCoreApplication.translate("MainWindow", u"Dar de baja un Proveedor (Alt+Supr)", None))
#endif // QT_CONFIG(tooltip)
        self.deleteProveedor.setText("")
#if QT_CONFIG(shortcut)
        self.deleteProveedor.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Del", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.searchProveedor.setToolTip(QCoreApplication.translate("MainWindow", u"Buscar Proveedor", None))
#endif // QT_CONFIG(tooltip)
        self.searchProveedor.setText("")
#if QT_CONFIG(tooltip)
        self.cleanProveedor.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar Proveedor (F6)", None))
#endif // QT_CONFIG(tooltip)
        self.cleanProveedor.setText("")
#if QT_CONFIG(shortcut)
        self.cleanProveedor.setShortcut(QCoreApplication.translate("MainWindow", u"F6", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Seleccione una opcion del lado izquiero para empezar.", None))
#if QT_CONFIG(tooltip)
        self.saveCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Guardar Cliente (F3)", None))
#endif // QT_CONFIG(tooltip)
        self.saveCliente.setText("")
#if QT_CONFIG(shortcut)
        self.saveCliente.setShortcut(QCoreApplication.translate("MainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.cancelOpCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#endif // QT_CONFIG(tooltip)
        self.cancelOpCliente.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Alta de Cliente", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Correo Electr\u00f3nico:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"R.F.C.:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.ID_cliente.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
#if QT_CONFIG(tooltip)
        self.modifyClienteConfirm.setToolTip(QCoreApplication.translate("MainWindow", u"Modificar Cliente (F3)", None))
#endif // QT_CONFIG(tooltip)
        self.modifyClienteConfirm.setText("")
#if QT_CONFIG(shortcut)
        self.modifyClienteConfirm.setShortcut(QCoreApplication.translate("MainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.cancelModifyCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#endif // QT_CONFIG(tooltip)
        self.cancelModifyCliente.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Detalle de Cliente", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.ID_cliente_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"R.F.C.:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Correo Electr\u00f3nico:", None))
#if QT_CONFIG(tooltip)
        self.deleteClienteConfirm.setToolTip(QCoreApplication.translate("MainWindow", u"Eliminar Cliente (F3)", None))
#endif // QT_CONFIG(tooltip)
        self.deleteClienteConfirm.setText("")
#if QT_CONFIG(shortcut)
        self.deleteClienteConfirm.setShortcut(QCoreApplication.translate("MainWindow", u"F3", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.cancelDeleteCliente.setToolTip(QCoreApplication.translate("MainWindow", u"Cancelar", None))
#endif // QT_CONFIG(tooltip)
        self.cancelDeleteCliente.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Baja de Cliente", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.ID_cliente_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"R.F.C.:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Correo Electr\u00f3nico:", None))
    # retranslateUi

