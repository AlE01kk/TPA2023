import sys
from PyQt6 import QtWidgets, uic
from VentanaPrincipal import Ui_VentanaPrincipal
from VentanaSecundaria import Ui_VentanaSecundaria
from mascota import Mascota

class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.guardar_mascota)
    
    def guardar_mascota(self):
        nombre = self.entrada_nombre.text()
        especie = self.entrada_especie.text()
        edad = self.entrada_edad.value()
        peso = self.entrada_peso.value()
        
        mascota = Mascota(nombre, especie, edad, peso)
        
        ventana_secundaria = VentanaSecundaria(mascota)
        ventana_secundaria.exec()

class VentanaSecundaria(QtWidgets.QDialog, Ui_VentanaSecundaria):
    def __init__(self, mascota, *args, **kwargs):
        super(VentanaSecundaria, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        self.label_2.setText(str(mascota))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ventana_principal = Ventana()
    ventana_principal.show()
    
    sys.exit(app.exec())
