import sys
import gramatica
from PyQt5           import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import Qt, QRect
from PyQt5.QtGui     import QColor, QPainter
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QAction, 
                             QVBoxLayout, QTabWidget, QFileDialog, QPlainTextEdit, QHBoxLayout,
                             QPushButton)
from PyQt5.QtCore import pyqtSlot

lineBarColor       = QColor(53, 53, 53)       
lineHighlightColor = QColor('#00FF04')        


class TabWidget(QTabWidget):

    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)

    # This virtual handler is called after a tab was removed from position index.   
    def tabRemoved(self, index):
        print("\n tab was removed from position index -> {}".format(index))

    # This virtual handler is called after a new tab was added or inserted at position index.        
    def tabInserted(self, index):
        print("\n New tab was added or inserted at position index -> {}".format(index))


#Clase para agregar los numeros
class NumberBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.editor = parent
        layout      = QVBoxLayout(self)
        self.editor.blockCountChanged.connect(self.update_width)
        self.editor.updateRequest.connect(self.update_on_scroll)
        self.update_width('001')   

    def mousePressEvent(self, QMouseEvent):
        print("\n - class NumberBar(QWidget): \n\tdef mousePressEvent(self, QMouseEvent):")

    def update_on_scroll(self, rect, scroll):
        if self.isVisible():
            if scroll:
                self.scroll(0, scroll)
            else:
                self.update()

    def update_width(self, string):
        width = self.fontMetrics().width(str(string)) + 10
        if self.width() != width:
            self.setFixedWidth(width)

    def paintEvent(self, event):
        if self.isVisible():
            block   = self.editor.firstVisibleBlock()
            height  = self.fontMetrics().height()
            number  = block.blockNumber()
            painter = QPainter(self)
            painter.fillRect(event.rect(), lineBarColor)
            painter.setPen(Qt.white)                       
            painter.drawRect(0, 0, event.rect().width() - 1, event.rect().height() - 1)
            font = painter.font()

            current_block = self.editor.textCursor().block().blockNumber() + 1

            while block.isValid():
                block_geometry = self.editor.blockBoundingGeometry(block)
                offset = self.editor.contentOffset()
                block_top = block_geometry.translated(offset).top()
                number += 1

                rect = QRect(0, block_top, self.width() - 5, height)

                if number == current_block:
                    font.setBold(True)
                else:
                    font.setBold(False)

                painter.setFont(font)
                painter.drawText(rect, Qt.AlignRight, '%i' % number)

                if block_top > event.rect().bottom():
                    break

                block = block.next()

            painter.end()


class Content(QWidget):
    def __init__(self, text):
        super(Content, self).__init__()
        
        self.editor = QPlainTextEdit()
        self.editor.setPlainText(text)#Setear el archivo al nuevo text edit
        self.consola = QPlainTextEdit()
        #self.consola.setPlainText()
        
        # Create a layout for the line numbers
        self.hbox    = QHBoxLayout(self)
        self.numbers = NumberBar(self.editor)
        self.hbox.addWidget(self.numbers)
        self.hbox.addWidget(self.editor)
        self.hbox.addWidget(self.consola)



class MyTableWidget(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = TabWidget()     #QTabWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeTab)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def closeTab(self, index):
        tab = self.tabs.widget(index)
        tab.deleteLater()
        self.tabs.removeTab(index)

    def addtab(self, content, fileName):
        self.tabs.addTab(Content(str(content)), str(fileName))


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.open()
        self.nuevo()
        self.save()
        self.saveAs()
        self.ascendente()
        self.tabs = MyTableWidget()
        self.setCentralWidget(self.tabs)
        self.initUI()
        self.show()

    def initUI(self):
        self.statusBar()
        menu = self.menuBar()
        fileMenu = menu.addMenu('Archivo')
        fileMenu.addAction(self.openAct)
        fileMenu.addAction(self.nuevoAct)
        fileMenu.addAction(self.saveAct)
        fileMenu.addAction(self.saveasAct)

        editMenu = menu.addMenu('Editar')

        ejecutarMenu = menu.addMenu('Ejecutar')
        ejecutarMenu.addAction(self.asceAct)

        reportesMenu = menu.addMenu('Reportes')
        apoyoMenu = menu.addMenu('Apoyo')
        ayudaMenu = menu.addMenu('Ayuda')

        self.resize(800, 600)

    def closeTab(self, index):
        tab = self.tabs.widget(index)
        tab.deleteLater()
        self.tabs.removeTab(index)

    def buttonClicked(self):
        self.tabs.addTab(Content("smalltext2"), "sadsad")

    #NUEVO ARCHIVO
    def nuevo(self):
        self.nuevoAct = QAction('Nuevo', self)
        self.nuevoAct.setShortcut('Ctrl+N')
        self.nuevoAct.setStatusTip('Open a file')
        self.is_opened = False
        self.nuevoAct.triggered.connect(self.newFile)
    
    #ABRIR ARCHIVO
    def open(self):
        self.openAct = QAction('Abrir', self)
        self.openAct.setShortcut('Ctrl+O')
        self.openAct.setStatusTip('Open a file')
        self.is_opened = False
        self.openAct.triggered.connect(self.openFile)
    
    #GUARDAR ARCHIVO
    def save(self):
        self.saveAct = QAction('Guardar', self)
        self.saveAct.setShortcut('Ctrl+S')
        self.saveAct.setStatusTip('Guardar archivo')
        #self.is_opened = False
        #self.saveAct.triggered.connect(self.openFile)

    #GUARDAR COMO ARCHIVO
    def saveAs(self):
        self.saveasAct = QAction('Guardar como', self)
        self.saveasAct.setShortcut('Ctrl+A')
        self.saveasAct.setStatusTip('Guardar archivo como')
        #self.is_opened = False
        #self.saveasAct.triggered.connect(self.openFile)

    #Ejecutar analizador ascendente
    def ascendente(self):
        self.asceAct = QAction('Ascendente', self)
        self.asceAct.setStatusTip('Ejecutando ascendente')
        self.is_opened = False
        self.asceAct.triggered.connect(self.runAsce)
        
    #BOTON ABRIR ARCHIVO
    def openFile(self):                                   
        options = QFileDialog.Options()
        filenames, _ = QFileDialog.getOpenFileNames(
            self, 'Open a file', '',
            'Python Files (*.py);;Text Files (*.txt)',
            options=options
        )
        if filenames:
            for filename in filenames:
                with open(filename, 'r+') as file_o:
                    try: 
                        text = file_o.read()
                        self.tabs.addtab(text, filename)      
                    except Exception as e:
                        print("Error: filename=`{}`, `{}` ".format( filename, str(e)))

    #BOTON NUEVO ARCHIVO
    def newFile(self):                                   
        options = QFileDialog.Options()
        text=""
        self.tabs.addtab(text, "file")

    #Funcion que se ejecuta tras presionar el boton de ascendente
    def runAsce(self):
        print("corrio run1")
        #text = self.tabs.addTab(Content.consola.toPlainText())
        #text = self.tabs.focusWidget(Content.editor.toPlainText)
        self.focusNextPrevChild(True)
        widget = QtWidgets.QApplication.focusWidget().children()
        codigo = widget[0].toPlainText()
        #text = QPlainTextEdit(widget)
        print(codigo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())