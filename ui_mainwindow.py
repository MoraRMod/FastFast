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
        icon.addFile(u":/icons/icon/fastfast.ico", QSize(), QIcon.Normal, QIcon.Off)
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
        self.iconHome.setIcon(icon)
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icon/bill.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/icon/bill_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconFactura.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icon/ticket.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icons/icon/ticket_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconPedido.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icon/products.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icon/products_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconAlimento.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/icon/customer.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icon/customer_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconClientes.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/icon/employee.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/icons/icon/employee_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconEmpleados.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/icon/supplier.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/icon/supplier_active.ico", QSize(), QIcon.Normal, QIcon.On)
        self.iconProveedor.setIcon(icon6)
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
        self.fullFactura.setIcon(icon1)
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
        self.fullPedido.setIcon(icon2)
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
        self.fullAlimento.setIcon(icon3)
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
        self.fullCliente.setIcon(icon4)
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
        self.fullEmpleado.setIcon(icon5)
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
        self.fullProveedor.setIcon(icon6)
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
        self.fullHome.setIcon(icon)
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icon/add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.addFactura.setIcon(icon7)
        self.addFactura.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.addFactura)

        self.modifyFactura = QPushButton(self.facturaWidget)
        self.modifyFactura.setObjectName(u"modifyFactura")
        self.modifyFactura.setEnabled(False)
        self.modifyFactura.setMinimumSize(QSize(40, 40))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icon/modify.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u":/icons/icon/modifyOff.ico", QSize(), QIcon.Disabled, QIcon.Off)
        self.modifyFactura.setIcon(icon8)
        self.modifyFactura.setIconSize(QSize(28, 28))

        self.horizontalLayout_2.addWidget(self.modifyFactura)

        self.deleteFactura = QPushButton(self.facturaWidget)
        self.deleteFactura.setObjectName(u"deleteFactura")
        self.deleteFactura.setEnabled(False)
        self.deleteFactura.setMinimumSize(QSize(40, 40))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icon/cancel.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u":/icons/icon/cancelOff.ico", QSize(), QIcon.Disabled, QIcon.Off)
        self.deleteFactura.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/icon/search.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.searchFactura.setIcon(icon10)
        self.searchFactura.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.searchFactura)

        self.cleanFactura = QPushButton(self.facturaWidget)
        self.cleanFactura.setObjectName(u"cleanFactura")
        self.cleanFactura.setMinimumSize(QSize(40, 40))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icon/reload.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cleanFactura.setIcon(icon11)
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
        self.addPedido.setIcon(icon7)
        self.addPedido.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.addPedido)

        self.modifyPedido = QPushButton(self.pedidoWidget)
        self.modifyPedido.setObjectName(u"modifyPedido")
        self.modifyPedido.setMinimumSize(QSize(40, 40))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icon/modify.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.modifyPedido.setIcon(icon12)
        self.modifyPedido.setIconSize(QSize(28, 28))

        self.horizontalLayout_3.addWidget(self.modifyPedido)

        self.deletePedido = QPushButton(self.pedidoWidget)
        self.deletePedido.setObjectName(u"deletePedido")
        self.deletePedido.setMinimumSize(QSize(40, 40))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icon/cancel.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.deletePedido.setIcon(icon13)
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
        self.searchPedido.setIcon(icon10)
        self.searchPedido.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.searchPedido)

        self.cleanPedido = QPushButton(self.pedidoWidget)
        self.cleanPedido.setObjectName(u"cleanPedido")
        self.cleanPedido.setMinimumSize(QSize(40, 40))
        self.cleanPedido.setIcon(icon11)
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
        self.addAlimento.setIcon(icon7)
        self.addAlimento.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.addAlimento)

        self.modifyAlimento = QPushButton(self.alimentosWidget)
        self.modifyAlimento.setObjectName(u"modifyAlimento")
        self.modifyAlimento.setMinimumSize(QSize(40, 40))
        self.modifyAlimento.setIcon(icon12)
        self.modifyAlimento.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.modifyAlimento)

        self.deleteAlimento = QPushButton(self.alimentosWidget)
        self.deleteAlimento.setObjectName(u"deleteAlimento")
        self.deleteAlimento.setMinimumSize(QSize(40, 40))
        self.deleteAlimento.setIcon(icon13)
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
        self.searchAlimento.setIcon(icon10)
        self.searchAlimento.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.searchAlimento)

        self.cleanAlimento = QPushButton(self.alimentosWidget)
        self.cleanAlimento.setObjectName(u"cleanAlimento")
        self.cleanAlimento.setMinimumSize(QSize(40, 40))
        self.cleanAlimento.setIcon(icon11)
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
        self.addCliente.setIcon(icon7)
        self.addCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.addCliente)

        self.modifyCliente = QPushButton(self.clientesWidget)
        self.modifyCliente.setObjectName(u"modifyCliente")
        self.modifyCliente.setMinimumSize(QSize(40, 40))
        self.modifyCliente.setIcon(icon12)
        self.modifyCliente.setIconSize(QSize(28, 28))

        self.horizontalLayout_5.addWidget(self.modifyCliente)

        self.deleteCliente = QPushButton(self.clientesWidget)
        self.deleteCliente.setObjectName(u"deleteCliente")
        self.deleteCliente.setMinimumSize(QSize(40, 40))
        self.deleteCliente.setIcon(icon13)
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
        self.searchCliente.setIcon(icon10)
        self.searchCliente.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.searchCliente)

        self.cleanCliente = QPushButton(self.clientesWidget)
        self.cleanCliente.setObjectName(u"cleanCliente")
        self.cleanCliente.setMinimumSize(QSize(40, 40))
        self.cleanCliente.setIcon(icon11)
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
        self.addEmpleado.setIcon(icon7)
        self.addEmpleado.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.addEmpleado)

        self.modifyEmpleado = QPushButton(self.empleadosWidget)
        self.modifyEmpleado.setObjectName(u"modifyEmpleado")
        self.modifyEmpleado.setMinimumSize(QSize(40, 40))
        self.modifyEmpleado.setIcon(icon12)
        self.modifyEmpleado.setIconSize(QSize(28, 28))

        self.horizontalLayout_7.addWidget(self.modifyEmpleado)

        self.deleteEmpleado = QPushButton(self.empleadosWidget)
        self.deleteEmpleado.setObjectName(u"deleteEmpleado")
        self.deleteEmpleado.setMinimumSize(QSize(40, 40))
        self.deleteEmpleado.setIcon(icon13)
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
        self.searchEmpleado.setIcon(icon10)
        self.searchEmpleado.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.searchEmpleado)

        self.cleanEmpleado = QPushButton(self.empleadosWidget)
        self.cleanEmpleado.setObjectName(u"cleanEmpleado")
        self.cleanEmpleado.setMinimumSize(QSize(40, 40))
        self.cleanEmpleado.setIcon(icon11)
        self.cleanEmpleado.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.cleanEmpleado)

        self.horizontalSpacer_7 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.gridLayout_7.addWidget(self.empleadosWidget, 0, 0, 1, 1)

        self.tableView = QTableView(self.pageEmpleados)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_7.addWidget(self.tableView, 1, 0, 1, 1)

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
        self.addProveedor.setIcon(icon7)
        self.addProveedor.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.addProveedor)

        self.modifyProveedor = QPushButton(self.proveedorWidget)
        self.modifyProveedor.setObjectName(u"modifyProveedor")
        self.modifyProveedor.setMinimumSize(QSize(40, 40))
        self.modifyProveedor.setIcon(icon12)
        self.modifyProveedor.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.modifyProveedor)

        self.deleteProveedor = QPushButton(self.proveedorWidget)
        self.deleteProveedor.setObjectName(u"deleteProveedor")
        self.deleteProveedor.setMinimumSize(QSize(40, 40))
        self.deleteProveedor.setIcon(icon13)
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
        self.searchProveedor.setIcon(icon10)
        self.searchProveedor.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.searchProveedor)

        self.cleanProveedor = QPushButton(self.proveedorWidget)
        self.cleanProveedor.setObjectName(u"cleanProveedor")
        self.cleanProveedor.setMinimumSize(QSize(40, 40))
        self.cleanProveedor.setIcon(icon11)
        self.cleanProveedor.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.cleanProveedor)

        self.horizontalSpacer_8 = QSpacerItem(505, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.gridLayout_8.addWidget(self.proveedorWidget, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.pageProveedores)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_8.addWidget(self.tableWidget, 1, 0, 1, 1)

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

        self.gridLayout.addWidget(self.multipleMenu, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.iconHome, self.fullHome)
        QWidget.setTabOrder(self.fullHome, self.iconFactura)
        QWidget.setTabOrder(self.iconFactura, self.iconPedido)
        QWidget.setTabOrder(self.iconPedido, self.iconAlimento)
        QWidget.setTabOrder(self.iconAlimento, self.iconClientes)
        QWidget.setTabOrder(self.iconClientes, self.iconEmpleados)
        QWidget.setTabOrder(self.iconEmpleados, self.iconProveedor)
        QWidget.setTabOrder(self.iconProveedor, self.fullFactura)
        QWidget.setTabOrder(self.fullFactura, self.fullPedido)
        QWidget.setTabOrder(self.fullPedido, self.fullAlimento)
        QWidget.setTabOrder(self.fullAlimento, self.fullCliente)
        QWidget.setTabOrder(self.fullCliente, self.fullEmpleado)
        QWidget.setTabOrder(self.fullEmpleado, self.fullProveedor)

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

        self.multipleMenu.setCurrentIndex(6)


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
    # retranslateUi

