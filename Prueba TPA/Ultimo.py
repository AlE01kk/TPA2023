import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal
from VentanaSecundaria import Ui_VentanaSecundaria
from mascota import Mascota


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Conexión del evento "clicked" del botón "Guardar Mascota" a la función guardar_mascota
        self.pushButton.clicked.connect(self.guardar_mascota)
    
    def guardar_mascota(self):
        # Recuperar la información de los componentes
        nombre = self.entrada_nombre.text()
        especie = self.entrada_especie.text()
        edad = self.entrada_edad.value()
        peso = self.entrada_peso.value()
        
        # Crear un objeto Mascota
        mascota = Mascota(nombre, especie, edad, peso)
        
        # Mostrar la información de la mascota en la ventana secundaria
        ventana_secundaria = VentanaSecundaria()
        ventana_secundaria.mostrar_informacion(mascota)
        ventana_secundaria.exec()


class VentanaSecundaria(QtWidgets.QDialog, Ui_VentanaSecundaria):
    def __init__(self, *args, obj=None, **kwargs):
        super(VentanaSecundaria, self).__init__(*args, **kwargs)
        self.setupUi(self)
    
    def mostrar_informacion(self, mascota):
        # Mostrar la información de la mascota en los componentes de la ventana secundaria
        self.label_2.setText(str(mascota))
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()
