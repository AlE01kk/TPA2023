# Form implementation generated from reading ui file 'ventanaprincipal.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(448, 338)
        self.centralwidget = QtWidgets.QWidget(parent=VentanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.entrada_peso = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget)
        self.entrada_peso.setObjectName("entrada_peso")
        self.gridLayout.addWidget(self.entrada_peso, 3, 1, 1, 1)
        self.entrada_especie = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.entrada_especie.setObjectName("entrada_especie")
        self.gridLayout.addWidget(self.entrada_especie, 1, 1, 1, 1)
        self.entrada_nombre = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.entrada_nombre.setObjectName("entrada_nombre")
        self.gridLayout.addWidget(self.entrada_nombre, 0, 1, 1, 1)
        self.entrada_edad = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget)
        self.entrada_edad.setObjectName("entrada_edad")
        self.gridLayout.addWidget(self.entrada_edad, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 36))
        self.menubar.setObjectName("menubar")
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=VentanaPrincipal)
        self.statusbar.setObjectName("statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "VentanaPrincipal"))
        self.label.setText(_translate("VentanaPrincipal", "Ingresar Datos Mascota"))
        self.label_2.setText(_translate("VentanaPrincipal", "Nombre"))
        self.label_5.setText(_translate("VentanaPrincipal", "Peso"))
        self.label_4.setText(_translate("VentanaPrincipal", "edad"))
        self.label_3.setText(_translate("VentanaPrincipal", "Especie"))
        self.pushButton.setText(_translate("VentanaPrincipal", "Guardar Mascota"))