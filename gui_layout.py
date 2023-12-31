# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 681)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(26, 10, 531, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.getColorRate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.getColorRate.setFont(font)
        self.getColorRate.setObjectName("getColorRate")
        self.verticalLayout_2.addWidget(self.getColorRate)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_showColorRate = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_showColorRate.setObjectName("lineEdit_showColorRate")
        self.verticalLayout_3.addWidget(self.lineEdit_showColorRate)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.getForecastByColor = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.getForecastByColor.setFont(font)
        self.getForecastByColor.setObjectName("getForecastByColor")
        self.verticalLayout_4.addWidget(self.getForecastByColor)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_getForecastByColor = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getForecastByColor.setObjectName("lineEdit_getForecastByColor")
        self.verticalLayout_5.addWidget(self.lineEdit_getForecastByColor)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.getBomInOrders = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.getBomInOrders.setFont(font)
        self.getBomInOrders.setObjectName("getBomInOrders")
        self.verticalLayout_6.addWidget(self.getBomInOrders)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lineEdit_getBomInOrder = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getBomInOrder.setObjectName("lineEdit_getBomInOrder")
        self.verticalLayout_7.addWidget(self.lineEdit_getBomInOrder)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.getPigComRate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.getPigComRate.setFont(font)
        self.getPigComRate.setAcceptDrops(False)
        self.getPigComRate.setAutoFillBackground(False)
        self.getPigComRate.setObjectName("getPigComRate")
        self.verticalLayout_8.addWidget(self.getPigComRate)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_getPigComRate = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getPigComRate.setObjectName("lineEdit_getPigComRate")
        self.verticalLayout_10.addWidget(self.lineEdit_getPigComRate)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.sales_Database = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.sales_Database.setFont(font)
        self.sales_Database.setAcceptDrops(False)
        self.sales_Database.setAutoFillBackground(False)
        self.sales_Database.setObjectName("sales_Database")
        self.verticalLayout_11.addWidget(self.sales_Database)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.lineEdit_sale_Database = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_sale_Database.setObjectName("lineEdit_sale_Database")
        self.verticalLayout_29.addWidget(self.lineEdit_sale_Database)
        self.verticalLayout_12.addLayout(self.verticalLayout_29)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.lineEdit_missedArticles = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_missedArticles.setObjectName("lineEdit_missedArticles")
        self.verticalLayout_30.addWidget(self.lineEdit_missedArticles)
        self.verticalLayout_12.addLayout(self.verticalLayout_30)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.align_sales_Database = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.align_sales_Database.setFont(font)
        self.align_sales_Database.setAcceptDrops(False)
        self.align_sales_Database.setAutoFillBackground(False)
        self.align_sales_Database.setObjectName("align_sales_Database")
        self.verticalLayout_13.addWidget(self.align_sales_Database)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.lineEdit_alignSale_Database = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_alignSale_Database.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_alignSale_Database.setObjectName("lineEdit_alignSale_Database")
        self.verticalLayout_31.addWidget(self.lineEdit_alignSale_Database)
        self.verticalLayout_14.addLayout(self.verticalLayout_31)
        self.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.lineEdit_alignSale_Database_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_alignSale_Database_1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_alignSale_Database_1.setText("")
        self.lineEdit_alignSale_Database_1.setObjectName("lineEdit_alignSale_Database_1")
        self.verticalLayout_32.addWidget(self.lineEdit_alignSale_Database_1)
        self.verticalLayout_14.addLayout(self.verticalLayout_32)
        self.horizontalLayout_6.addLayout(self.verticalLayout_14)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSpacing(7)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.getcurrentorder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.getcurrentorder.setFont(font)
        self.getcurrentorder.setAcceptDrops(False)
        self.getcurrentorder.setAutoFillBackground(False)
        self.getcurrentorder.setObjectName("getcurrentorder")
        self.verticalLayout_15.addWidget(self.getcurrentorder)
        self.horizontalLayout_7.addLayout(self.verticalLayout_15)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.lineEdit_getcurrentorder = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getcurrentorder.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_getcurrentorder.setText("")
        self.lineEdit_getcurrentorder.setObjectName("lineEdit_getcurrentorder")
        self.verticalLayout_33.addWidget(self.lineEdit_getcurrentorder)
        self.verticalLayout_16.addLayout(self.verticalLayout_33)
        self.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.lineEdit_missedArticleOrdervsData = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_missedArticleOrdervsData.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_missedArticleOrdervsData.setText("")
        self.lineEdit_missedArticleOrdervsData.setObjectName("lineEdit_missedArticleOrdervsData")
        self.verticalLayout_34.addWidget(self.lineEdit_missedArticleOrdervsData)
        self.verticalLayout_16.addLayout(self.verticalLayout_34)
        self.horizontalLayout_7.addLayout(self.verticalLayout_16)
        self.horizontalLayout_7.setStretch(0, 3)
        self.horizontalLayout_7.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.alignOrderData = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.alignOrderData.setFont(font)
        self.alignOrderData.setAcceptDrops(False)
        self.alignOrderData.setAutoFillBackground(False)
        self.alignOrderData.setObjectName("alignOrderData")
        self.verticalLayout_17.addWidget(self.alignOrderData)
        self.horizontalLayout_8.addLayout(self.verticalLayout_17)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.lineEdit_alignOrder_Database = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_alignOrder_Database.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_alignOrder_Database.setObjectName("lineEdit_alignOrder_Database")
        self.verticalLayout_35.addWidget(self.lineEdit_alignOrder_Database)
        self.verticalLayout_18.addLayout(self.verticalLayout_35)
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.lineEdit_alignOrder_Database1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_alignOrder_Database1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_alignOrder_Database1.setText("")
        self.lineEdit_alignOrder_Database1.setObjectName("lineEdit_alignOrder_Database1")
        self.verticalLayout_36.addWidget(self.lineEdit_alignOrder_Database1)
        self.verticalLayout_18.addLayout(self.verticalLayout_36)
        self.horizontalLayout_8.addLayout(self.verticalLayout_18)
        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.historyConsum = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.historyConsum.setFont(font)
        self.historyConsum.setAcceptDrops(False)
        self.historyConsum.setAutoFillBackground(False)
        self.historyConsum.setObjectName("historyConsum")
        self.verticalLayout_19.addWidget(self.historyConsum)
        self.horizontalLayout_9.addLayout(self.verticalLayout_19)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.lineEdit_historyConsum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_historyConsum.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_historyConsum.setText("")
        self.lineEdit_historyConsum.setObjectName("lineEdit_historyConsum")
        self.verticalLayout_20.addWidget(self.lineEdit_historyConsum)
        self.horizontalLayout_9.addLayout(self.verticalLayout_20)
        self.horizontalLayout_9.setStretch(0, 3)
        self.horizontalLayout_9.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.getIntransit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.getIntransit.setFont(font)
        self.getIntransit.setAcceptDrops(False)
        self.getIntransit.setAutoFillBackground(False)
        self.getIntransit.setObjectName("getIntransit")
        self.verticalLayout_21.addWidget(self.getIntransit)
        self.horizontalLayout_10.addLayout(self.verticalLayout_21)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.lineEdit_getIntransit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getIntransit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_getIntransit.setText("")
        self.lineEdit_getIntransit.setObjectName("lineEdit_getIntransit")
        self.verticalLayout_22.addWidget(self.lineEdit_getIntransit)
        self.horizontalLayout_10.addLayout(self.verticalLayout_22)
        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.getChemicalStock = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.getChemicalStock.setFont(font)
        self.getChemicalStock.setAcceptDrops(False)
        self.getChemicalStock.setAutoFillBackground(False)
        self.getChemicalStock.setObjectName("getChemicalStock")
        self.verticalLayout_23.addWidget(self.getChemicalStock)
        self.horizontalLayout_11.addLayout(self.verticalLayout_23)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.lineEdit_getChemicalStock = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_getChemicalStock.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_getChemicalStock.setText("")
        self.lineEdit_getChemicalStock.setObjectName("lineEdit_getChemicalStock")
        self.verticalLayout_24.addWidget(self.lineEdit_getChemicalStock)
        self.horizontalLayout_11.addLayout(self.verticalLayout_24)
        self.horizontalLayout_11.setStretch(0, 3)
        self.horizontalLayout_11.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.allthingtogether = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.allthingtogether.setFont(font)
        self.allthingtogether.setAcceptDrops(False)
        self.allthingtogether.setAutoFillBackground(False)
        self.allthingtogether.setObjectName("allthingtogether")
        self.verticalLayout_25.addWidget(self.allthingtogether)
        self.horizontalLayout_13.addLayout(self.verticalLayout_25)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem11)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.lineEdit_allthingtogether = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_allthingtogether.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_allthingtogether.setText("")
        self.lineEdit_allthingtogether.setObjectName("lineEdit_allthingtogether")
        self.verticalLayout_26.addWidget(self.lineEdit_allthingtogether)
        self.horizontalLayout_13.addLayout(self.verticalLayout_26)
        self.horizontalLayout_13.setStretch(0, 3)
        self.horizontalLayout_13.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.RunSolve = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(9)
        self.RunSolve.setFont(font)
        self.RunSolve.setAcceptDrops(False)
        self.RunSolve.setAutoFillBackground(False)
        self.RunSolve.setObjectName("RunSolve")
        self.verticalLayout_27.addWidget(self.RunSolve)
        self.horizontalLayout_14.addLayout(self.verticalLayout_27)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.lineEdit_RunSolve = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_RunSolve.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_RunSolve.setText("")
        self.lineEdit_RunSolve.setObjectName("lineEdit_RunSolve")
        self.verticalLayout_28.addWidget(self.lineEdit_RunSolve)
        self.horizontalLayout_14.addLayout(self.verticalLayout_28)
        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chemical Control"))
        self.getColorRate.setText(_translate("MainWindow", "get Color Rate"))
        self.getForecastByColor.setText(_translate("MainWindow", "get Forecast By Color"))
        self.getBomInOrders.setText(_translate("MainWindow", "get BOM In Order"))
        self.getPigComRate.setText(_translate("MainWindow", "Pig Com Rate"))
        self.sales_Database.setText(_translate("MainWindow", "Sale vs Database"))
        self.align_sales_Database.setText(_translate("MainWindow", "Align Sale Database"))
        self.lineEdit_alignSale_Database.setText(_translate("MainWindow", "Name to replace"))
        self.getcurrentorder.setText(_translate("MainWindow", "CurOrder vs Database"))
        self.alignOrderData.setText(_translate("MainWindow", "Align Order Database"))
        self.lineEdit_alignOrder_Database.setText(_translate("MainWindow", "Name to replace"))
        self.historyConsum.setText(_translate("MainWindow", "Get History ConSum"))
        self.getIntransit.setText(_translate("MainWindow", "Get Intransit"))
        self.getChemicalStock.setText(_translate("MainWindow", "Get Chemical Stock"))
        self.allthingtogether.setText(_translate("MainWindow", "All Things Together"))
        self.RunSolve.setText(_translate("MainWindow", "RunSovle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
