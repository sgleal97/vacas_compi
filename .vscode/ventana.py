from tkinter import *

ventana = Tk()

#Opciones de raiz o contenedor
ventana.title("Augus")
ventana.geometry("900x700")

#Opciones de Frame
miFrame=Frame()
miFrame.pack()

#Crear barra de menu
barraMenu=Menu(miFrame)
#Crear los menus
menuArchivo=Menu(barraMenu, tearoff=0)
menuEditar=Menu(barraMenu, tearoff=0)
menuEjecutar=Menu(barraMenu, tearoff=0)
menuAscendente=Menu(barraMenu, tearoff=0)
menuErrores=Menu(barraMenu, tearoff=0)
menuOpciones=Menu(barraMenu, tearoff=0)
menuAyuda=Menu(barraMenu, tearoff=0)
#Crear opciones de menu
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Guardar")
menuArchivo.add_command(label="Guardar Como")
menuArchivo.add_command(label="Cerrar")
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir")

menuEditar.add_command(label="Copiar")
menuEditar.add_command(label="Cortar")
menuEditar.add_command(label="Pegar")
menuEditar.add_separator()
menuEditar.add_command(label="Buscar")

#Agregar barra de menu "Ascendente"
menuAscendente.add_command(label="Correr")
menuAscendente.add_command(label="Debugger")
menuEjecutar.add_cascade(label="Ascendente", menu=menuAscendente)
menuEjecutar.add_command(label="Descendente")
menuEjecutar.add_separator()
#Agregar barra de menu de "errores"
menuErrores.add_command(label="Lexico")
menuErrores.add_command(label="Sintactico")
menuErrores.add_command(label="Lexico")
menuEjecutar.add_cascade(label="Errores", menu=menuErrores)

menuEjecutar.add_command(label="Tabla de simbolos")
menuEjecutar.add_command(label="AST")
menuEjecutar.add_command(label="Reporte gramatical")

menuOpciones.add_command(label="Cambiar color")
menuOpciones.add_command(label="Quitar No. Lineas")

menuAyuda.add_command(label="Ayuda")
menuAyuda.add_command(label="Acerca de")

#Agregar a barra de menu
barraMenu.add_cascade(label="Archivo",menu=menuArchivo)
barraMenu.add_cascade(label="Editar",menu=menuEditar)
barraMenu.add_cascade(label="Ejecutar",menu=menuEjecutar)
barraMenu.add_cascade(label="Opciones",menu=menuOpciones)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
#Agregamos la barra de menu a la ventana
ventana.config(menu=barraMenu)

#def abrirArchivo


ventana.mainloop()