import sys
from PyQt5 import uic 
from PyQt5.QtWidgets import QMainWindow, QApplication

class interfaz_gui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("C:\\Users\\sergi\\Desktop\\GUI\\interfaz.ui", self)
        self.pestanias = [] #array que almacenara las pestanias
        self.index = 0 #Contador de numero de pestanias
        
        self.btn_mas.clicked.connect(self.nueva_pestania)

    def nueva_pestania(self):
        if len(self.pestanias) > 0:
            for i in range(len(self.pestanias)):
                self.index = i + 1
        self.tabWidget.addTab(self.pestanias[self.index], "")
        #Poner el foco en el nuevo tab
        self.tabWidget.setCurrentIndex(self.index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = interfaz_gui()
    GUI.show()
    sys.exit(app.exec_())

