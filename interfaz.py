# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import subprocess

#from gramatica import *
from asc import *
import pila as PILA

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QDir, QFileDialog
contador = 1

import threading, time

def cmd(commando):
    subprocess.run(commando, shell=True)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1155, 859)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1131, 781))
        self.tabWidget.setAcceptDrops(False)

        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)

        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.btn_asce = QtWidgets.QPushButton(self.tab)
        self.btn_asce.setGeometry(QtCore.QRect(30, 20, 61, 23))
        self.btn_asce.setObjectName("btn_asce")
        self.btn_asce.clicked.connect(self.analisisAscendente)

        self.btn_desc = QtWidgets.QPushButton(self.tab)
        self.btn_desc.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.btn_desc.setObjectName("btn_desc")
        self.btn_desc.clicked.connect(self.analisisDescendente)

        self.btn_debu = QtWidgets.QPushButton(self.tab)
        self.btn_debu.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.btn_debu.setObjectName("btn_debu")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(30, 70, 1081, 451))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 540, 1081, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab, "")

        #self.textEdit_2.returnPressed.connect(self.obtenerTexto)
        #self.textEdit_2.textChanged.connect(self.cambioTexto)
        #self.textEdit_2.keyPressEvent = self.keyPressEvent


        self.btn_mas = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mas.setGeometry(QtCore.QRect(1070, 10, 21, 21))
        self.btn_mas.setObjectName("btn_mas")
        self.btn_mas.clicked.connect(self.newTab)

        self.btn_menos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_menos.setGeometry(QtCore.QRect(1100, 10, 21, 21))
        self.btn_menos.setObjectName("btn_menos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1155, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuOpcines = QtWidgets.QMenu(self.menubar)
        self.menuOpcines.setObjectName("menuOpcines")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuAscendente = QtWidgets.QMenu(self.menuAyuda)
        self.menuAscendente.setObjectName("menuAscendente")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        self.menuErrores = QtWidgets.QMenu(self.menuReportes)
        self.menuErrores.setObjectName("menuErrores")
        self.menuAST = QtWidgets.QMenu(self.menuReportes)
        self.menuAST.setObjectName("menuAST")
        self.menuEjecutar = QtWidgets.QMenu(self.menubar)
        self.menuEjecutar.setObjectName("menuEjecutar")
        self.menuAyuda_2 = QtWidgets.QMenu(self.menubar)
        self.menuAyuda_2.setObjectName("menuAyuda_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionNuevo.triggered.connect(self.newTab)

        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionAbrir.triggered.connect(self.openFile)

        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionCerrar = QtWidgets.QAction(MainWindow)
        self.actionCerrar.setObjectName("actionCerrar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCambiar_color = QtWidgets.QAction(MainWindow)
        self.actionCambiar_color.setObjectName("actionCambiar_color")
        self.actionQuitar_numero_de_lineas = QtWidgets.QAction(MainWindow)
        self.actionQuitar_numero_de_lineas.setObjectName("actionQuitar_numero_de_lineas")
        self.actionAcerca_de = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de.setObjectName("actionAcerca_de")

        self.actionTabla_de_simbolos = QtWidgets.QAction(MainWindow)
        self.actionTabla_de_simbolos.setObjectName("actionTabla_de_simbolos")
        self.actionTabla_de_simbolos.triggered.connect(self.reporteTS)

        self.actionAST = QtWidgets.QAction(MainWindow)
        self.actionAST.setObjectName("actionAST")

        self.actionReporte_gramatical = QtWidgets.QAction(MainWindow)
        self.actionReporte_gramatical.setObjectName("actionReporte_gramatical")
        self.actionReporte_gramatical.triggered.connect(self.reporteGramatical)

        self.actionLexicos = QtWidgets.QAction(MainWindow)
        self.actionLexicos.setObjectName("actionLexicos")
        self.actionLexicos.triggered.connect(self.reporteErrorLexico)


        self.actionSintacticos = QtWidgets.QAction(MainWindow)
        self.actionSintacticos.setObjectName("actionSintacticos")
        self.actionSintacticos.triggered.connect(self.reporteErrorSintactico)

        self.actionSemanticos = QtWidgets.QAction(MainWindow)
        self.actionSemanticos.setObjectName("actionSemanticos")

        self.actionPegar = QtWidgets.QAction(MainWindow)
        self.actionPegar.setObjectName("actionPegar")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionDebugger = QtWidgets.QAction(MainWindow)
        self.actionDebugger.setObjectName("actionDebugger")
        self.actionCambiar_color_2 = QtWidgets.QAction(MainWindow)
        self.actionCambiar_color_2.setObjectName("actionCambiar_color_2")
        self.actionQuitar_numero_de_lineas_2 = QtWidgets.QAction(MainWindow)
        self.actionQuitar_numero_de_lineas_2.setObjectName("actionQuitar_numero_de_lineas_2")
        self.actionAyuda_2 = QtWidgets.QAction(MainWindow)
        self.actionAyuda_2.setObjectName("actionAyuda_2")
        self.actionAcerca_de_2 = QtWidgets.QAction(MainWindow)
        self.actionAcerca_de_2.setObjectName("actionAcerca_de_2")
        self.actionAscendente = QtWidgets.QAction(MainWindow)
        self.actionAscendente.setObjectName("actionAscendente")
        
        self.actionDescendente = QtWidgets.QAction(MainWindow)
        self.actionDescendente.setObjectName("actionDescendente")
        self.actionDescendente.triggered.connect(self.reporteASTASC)

        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_como)
        self.menuArchivo.addAction(self.actionCerrar)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuOpcines.addAction(self.actionCambiar_color)
        self.menuOpcines.addAction(self.actionQuitar_numero_de_lineas)
        self.menuOpcines.addAction(self.actionPegar)
        self.menuAscendente.addAction(self.actionRun)
        self.menuAscendente.addAction(self.actionDebugger)
        self.menuAyuda.addAction(self.menuAscendente.menuAction())
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menuErrores.addAction(self.actionLexicos)
        self.menuErrores.addAction(self.actionSintacticos)
        self.menuErrores.addAction(self.actionSemanticos)
        self.menuAST.addAction(self.actionAscendente)
        self.menuAST.addAction(self.actionDescendente)
        self.menuReportes.addAction(self.menuErrores.menuAction())
        self.menuReportes.addAction(self.actionTabla_de_simbolos)
        self.menuReportes.addAction(self.menuAST.menuAction())
        self.menuReportes.addAction(self.actionReporte_gramatical)
        self.menuEjecutar.addAction(self.actionCambiar_color_2)
        self.menuEjecutar.addAction(self.actionQuitar_numero_de_lineas_2)
        self.menuAyuda_2.addAction(self.actionAyuda_2)
        self.menuAyuda_2.addAction(self.actionAcerca_de_2)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOpcines.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuEjecutar.menuAction())
        self.menubar.addAction(self.menuAyuda_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def newTab(self):
        global contador
        contador  = contador + 1


        tab = QtWidgets.QWidget()
        tab.setObjectName("tab")
        
        btn_asce = QtWidgets.QPushButton(tab)
        btn_asce.setGeometry(QtCore.QRect(30, 20, 61, 23))
        btn_asce.setObjectName("btn_asce")
        btn_asce.setText("Ascendente")
        btn_asce.clicked.connect(self.analisisAscendente)

        btn_desc = QtWidgets.QPushButton(tab)
        btn_desc.setGeometry(QtCore.QRect(100, 20, 75, 23))
        btn_desc.setObjectName("btn_desc")
        btn_desc.setText("Descendente")

        btn_debu = QtWidgets.QPushButton(tab)
        btn_debu.setGeometry(QtCore.QRect(180, 20, 75, 23))
        btn_debu.setObjectName("btn_debu")
        btn_debu.setText("Debugger")

        textEdit = QtWidgets.QTextEdit(tab)
        textEdit.setGeometry(QtCore.QRect(30, 70, 1081, 451))
        textEdit.setObjectName("textEdit")

        textEdit_2 = QtWidgets.QTextEdit(tab)
        textEdit_2.setGeometry(QtCore.QRect(30, 540, 1081, 191))
        textEdit_2.setObjectName("textEdit_2")

        self.tabWidget.addTab(tab, "New"+str(contador))

    def closeTab(self, index):
        global contador
        contador = contador - 1
        tab = self.tabWidget.widget(index)
        tab.deleteLater()
        self.tabWidget.removeTab(index)

    def analisisAscendente(self):
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        texto = items[3].toPlainText()
        analisisAsc = Main(texto, items[4])

    def analisisDescendente(self):
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        texto = items[3].toPlainText()
        analisisDesc = Main2(texto, items[4])

    def openFile(self):                        
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()

        if dialog.exec_():
            file_name=dialog.selectedFiles()

            if file_name[0].endswith('.py'):
                with open(file_name[0], 'r+') as f:
                    data=f.read()
                    items[3].setPlainText(data)
                    f.close
            elif file_name[0].endswith('.txt'):
                with open(file_name[0], 'r+') as f:
                    data=f.read()
                    items[3].setPlainText(data)
                    f.close
            else:
                pass

    def cambioTexto(self):
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        if(items[4].hasFocus()):
            print("Cambio de texto en textEdit")
            print( self.textEdit_2.toPlainText())

    #def keyPressEvent(self, event):
    #        return QtWidgets.QTextEdit.keyPressEvent(self.textEdit_2, event)

    def reporteErrorLexico(self):
        lexicos = PILA.Pila()
        lexicos = g.errorLexicos
        lex = ""
        lex += "digraph H {\n"
        lex += "aHtmlTable [\n"
        lex += "shape=plaintext\n"
        lex += "label=<\n"
        lex += "<table border='1' cellborder='1'>\n"
        lex += "<tr>\n"
        lex += "<td>VALOR</td>\n"
        lex += "<td>TIPO</td>\n"
        lex += "<td>FILA</td>\n"
        lex += "<td>COLUMNA</td>\n"
        lex += "</tr>\n"
        while lexicos.estaVacia() == False:
            Diccionario = lexicos.pop()
            lex+="<tr>\n"
            lex += "<td>"+ str(Diccionario['Error']) + "</td>\n"
            lex += "<td>"+ str(Diccionario['Tipo']) + "</td>\n"
            lex += "<td>"+ str(Diccionario['Fila']) + "</td>\n"
            lex += "<td>"+ str(Diccionario['Columna']) + "</td>\n"
            lex += "</tr>\n"
        lex += "</table>\n"
        lex += ">];\n"
        lex += "}\n"
        f = open("lexicos.dot", "w")
        f.write(lex)
        f.close()
        cmd("dot -Tpng lexicos.dot -o lexicos.png")
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        items[4].append("***********Se genero el reporte de errores lexicos***************")
    
    def reporteErrorSintactico(self):
        sintactivos = PILA.Pila()
        sintactivos = g.erroresSintacticos
        sintac = " "
        sintac += "digraph H {\n"
        sintac += "aHtmlTable [\n"
        sintac += "shape=plaintext\n"
        sintac += "label=<\n"
        sintac += "<table border='1' cellborder='1'>\n"
        sintac += "<tr>\n"
        sintac += "<td>VALOR</td>\n"
        sintac += "<td>TIPO</td>\n"
        sintac += "<td>FILA</td>\n"
        sintac += "<td>COLUMNA</td>\n"
        sintac += "</tr>\n"
        while sintactivos.estaVacia() == False:
            Diccionario = sintactivos.pop()
            sintac+="<tr>\n"
            sintac += "<td>"+ str(Diccionario['Error']) + "</td>\n"
            sintac += "<td>"+ str(Diccionario['Tipo']) + "</td>\n"
            sintac += "<td>"+ str(Diccionario['Fila']) + "</td>\n"
            sintac += "<td>"+ str(Diccionario['Columna']) + "</td>\n"
            sintac += "</tr>\n"
        sintac += "</table>\n"
        sintac += ">];\n"
        sintac += "}\n"
        f = open("sintacticos.dot", "w")
        f.write(sintac)
        f.close()
        cmd("dot -Tpng sintacticos.dot -o sintactico.png")
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        items[4].append("***********Se genero el reporte de errores sintacticos***************")

    def reporteGramatical(self):
        gramatical = PILA.Pila()
        gramatical = g.reporteGramatical
        gram = " "
        gram += "digraph H {\n"
        gram += "aHtmlTable [\n"
        gram += "shape=plaintext\n"
        gram += "label=<\n"
        gram += "<table border='1' cellborder='1'>\n"
        gram += "<tr>\n"
        gram += "<td>Produccion</td>\n"
        gram += "<td>Derivacion</td>\n"
        gram += "<td>Regla semantica</td>\n"
        gram += "</tr>\n"
        while gramatical.estaVacia() == False:
            Diccionario = gramatical.pop()
            gram+="<tr>\n"
            gram += "<td>"+ str(Diccionario['produccion']) + "</td>\n"
            gram += "<td>"+ str(Diccionario['regla']) + "</td>\n"
            gram += "<td>"+ str(Diccionario['semantica']) + "</td>\n"
            gram += "</tr>\n"
        gram += "</table>\n"
        gram += ">];\n"
        gram += "}\n"
        f = open("gramatical.dot", "w")
        f.write(gram)
        f.close()
        cmd("dot -Tpng gramatical.dot -o gramatical.png")
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        items[4].append("***********Se genero el reporte gramatical***************")

    def reporteASTASC(self):
        astAsc()
        cmd("dot -Tpng asc.dot -o asc.png")
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        items[4].append("***********Se genero el reporte el arbol ast***************")

    def reporteTS(self):
        cmd("dot -Tpng tsg.dot -o tsg.png")
        tab = self.tabWidget.widget(self.tabWidget.currentIndex())
        items = tab.children()
        items[4].append("***********Se genero el reporte de la tabla de simbolos***************")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_asce.setText(_translate("MainWindow", "Ascendente"))
        self.btn_desc.setText(_translate("MainWindow", "Descendente"))
        self.btn_debu.setText(_translate("MainWindow", "Debugger"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page"))
        self.btn_mas.setText(_translate("MainWindow", "+"))
        self.btn_menos.setText(_translate("MainWindow", "-"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuOpcines.setTitle(_translate("MainWindow", "Editar"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ejecutar"))
        self.menuAscendente.setTitle(_translate("MainWindow", "Ascendente"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.menuErrores.setTitle(_translate("MainWindow", "Errores"))
        self.menuAST.setTitle(_translate("MainWindow", "AST"))
        self.menuEjecutar.setTitle(_translate("MainWindow", "Opciones"))
        self.menuAyuda_2.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_como.setText(_translate("MainWindow", "Guardar como"))
        self.actionCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionCambiar_color.setText(_translate("MainWindow", "Cambiar color"))
        self.actionQuitar_numero_de_lineas.setText(_translate("MainWindow", "Quitar numero de lineas"))
        self.actionAcerca_de.setText(_translate("MainWindow", "Descendente"))
        self.actionTabla_de_simbolos.setText(_translate("MainWindow", "Tabla de simbolos"))
        self.actionReporte_gramatical.setText(_translate("MainWindow", "Reporte gramatical"))
        self.actionLexicos.setText(_translate("MainWindow", "Lexicos"))
        self.actionSintacticos.setText(_translate("MainWindow", "Sintacticos"))
        self.actionSemanticos.setText(_translate("MainWindow", "Semanticos"))
        self.actionPegar.setText(_translate("MainWindow", "Pegar"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionDebugger.setText(_translate("MainWindow", "Debugger"))
        self.actionCambiar_color_2.setText(_translate("MainWindow", "Cambiar color"))
        self.actionQuitar_numero_de_lineas_2.setText(_translate("MainWindow", "Quitar numero de lineas"))
        self.actionAyuda_2.setText(_translate("MainWindow", "Ayuda"))
        self.actionAcerca_de_2.setText(_translate("MainWindow", "Acerca de"))
        self.actionAscendente.setText(_translate("MainWindow", "Ascendente"))
        self.actionDescendente.setText(_translate("MainWindow", "Descendente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())