import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ventana_1 import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Inicializar la interfaz generada por Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar eventos o realizar otras configuraciones
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
