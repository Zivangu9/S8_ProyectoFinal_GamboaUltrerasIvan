from tkinter import *				
from tkinter import messagebox
from tkinter import ttk
from connection import *
from validacion import *
from tablas import *
from libros import *
from usuarios import *
import textwrap
from tkinter.scrolledtext import *
from tkcalendar import *
from datetime import *
import matplotlib,numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
import matplotlib.pylab as pl
import webbrowser as wb
from reportlab.lib.pagesizes import *
from reportlab.lib.fonts import *
from reportlab.pdfgen import canvas
import itertools
import os
font =("Bookman Old Style", 12)
window = register = login = libro = admin = opcionesGraf = grafica = reporte = None
notebook = None
tabla_galeria = tabla_coleccion = tabla_deseados = tabla_leidos = None
id_user = id_libro = None
usuarioColecValue = usuarioDeseadValue = usuarioLeidosValue = infousuario = None
btnObtenido = btnDeseado = btnLeido = None
btnGrafica = btnReporte = None
conn = Connection()
def destroyAll():
	global window, register, login, libro, admin, opcionesGraf, reporte
	if not(register is None):
		try:
			register.destroy()
		except:
			pass
	if not(login is None):
		try:
			login.destroy()
		except:
			pass
	if not(libro is None):
		try:
			libro.destroy()
		except:
			pass
	if not(admin is None):
		try:
			admin.destroy()
		except:
			pass
	if not(opcionesGraf is None):
		try:
			opcionesGraf.destroy()
		except:
			pass
	if not(grafica is None):
		try:
			grafica.destroy()
		except:
			pass
	if not(reporte is None):
		try:
			reporte.destroy()
		except:
			pass
	if not(window is None):
		try:
			window.destroy()
		except:
			pass
def cerrarAdmin():
	global libro, admin
	if not(admin is None):
		try:
			admin.destroy()
		except:
			pass
	if not(libro is None):
		try:
			libro.destroy()
		except:
			pass
		libro = None
def iniciarApp(id_u):
	global window, register, login, id_user, font
	id_user = id_u
	if not(register is None):
		register.destroy()
		register = None
	if not(login is None):
		login.destroy()
		login = None
	window = Tk()
	window.option_add("*Font",font)
	centrar(window,990,510) 
	window.resizable(False, False)
	window.title('My Book Collection')
	informacionUsuario(id_u)
	menuprincipal(id_u)
	window.protocol("WM_DELETE_WINDOW", destroyAll)
	text = Text(window,font = ("Bookman Old Style",12))
	window.mainloop()
def tab_switch(event):
	global tabla_galeria, conn,btnGrafica, btnReporte
	if notebook.tab(notebook.select(), "text") == "Salir":
		id_user = None
		showLogin()
	if notebook.tab(notebook.select(), "text") == "Galería" or notebook.tab(notebook.select(), "text") == "Deseados":
		btnGrafica.grid_forget()
		btnReporte.grid_forget()
	else:
		btnGrafica.grid(row=0,column=0,padx=(10,10),pady=(10,10))
		btnReporte.grid(row=0,column=1,padx=(10,10),pady=(10,10))
	actualizarInformacion()
def actualizarInformacion():
	global tabla_galeria, tabla_coleccion, tabla_deseados, tabla_leidos, id_user
	actualizarTabla(tabla_galeria,consultarLibros(conn))
	actualizarTablaLista(tabla_coleccion,consultarLibrosObtenidos(conn,id_user))
	actualizarTablaLista(tabla_deseados,consultarLibrosDeseados(conn,id_user))
	actualizarTablaLista(tabla_leidos,consultarLibrosLeidos(conn,id_user))
	actualizarCantidades()
def informacionUsuario(id_u):
	global usuarioColecValue, usuarioDeseadValue, usuarioLeidosValue, infousuario, id_user, window
	infousuario = Frame(window)
	infousuario.grid(row=0,column=0)
	nombreFrame = Frame(infousuario)
	nombreFrame.grid(row=0,column=0,columnspan=6)
	usuarioLabel = Label(nombreFrame,text="Usuario:",anchor="e",width=12).grid(row=0, column=0)  
	usuarioColecLabel = Label(infousuario,text="Libros Obtenidos:",anchor="e",width=15).grid(row=1, column=0)  
	usuarioDeseadLabel = Label(infousuario,text="Libros Deseados:",anchor="e",width=17).grid(row=1, column=2)  
	usuarioLeidosLabel = Label(infousuario,text="Libros Leídos:",anchor="e",width=15).grid(row=1, column=4)  
	usuarioValue = Label(nombreFrame,text=consultarNombre(conn,id_u),anchor="w",width=30).grid(row=0, column=1)
	actualizarCantidades()
def treeViewListener(event):
	tree = event.widget
	showLibro(tree.item(tree.selection(),'text'))
def actualizarCantidades():
	global usuarioColecValue, usuarioDeseadValue, usuarioLeidosValue, infousuario, id_user
	usuarioColecValue = Label(infousuario,text=cantidadLibrosObtenidos(conn,id_user),underline = True).grid(row=1, column=1)
	usuarioDeseadValue = Label(infousuario,text=cantidadLibrosDeseados(conn,id_user)).grid(row=1, column=3)
	usuarioLeidosValue = Label(infousuario,text=cantidadLibrosLeidos(conn,id_user)).grid(row=1, column=5)
def menuprincipal(id_u):
	global notebook, conn, tabla_galeria, tabla_coleccion, tabla_deseados, tabla_leidos, font, window
	global btnGrafica, btnReporte
	botonesGenerar = Frame(window,width=193, height = 106)
	botonesGenerar.grid(row=0,column=1)
	iconGrafica = PhotoImage(file="img/grafica.png")
	iconGrafica = iconGrafica.subsample(10, 10)
	btnGrafica = Button(botonesGenerar,text = "Graficar",image=iconGrafica,compound=TOP,command=showOpcionesGrafica)
	btnGrafica.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	iconReporte = PhotoImage(file="img/reporte.png")
	iconReporte = iconReporte.subsample(10, 10)
	btnReporte = Button(botonesGenerar,text = "Reporte",image=iconReporte,compound=TOP,command=showCrearReporte)
	btnReporte.grid(row=0,column=1,padx=(10,10),pady=(10,10))
	style = ttk.Style(window)
	style.configure('lefttab.TNotebook', tabposition='ws')
	style.configure('lefttab.TNotebook.Tab', margin = 10, padding = [10,20])
	notebook = ttk.Notebook(window, style='lefttab.TNotebook',width=900,height=400)
	tab_galeria = ttk.Frame(notebook)
	tab_coleccion = ttk.Frame(notebook)
	tab_deseados = ttk.Frame(notebook)
	tab_leidos = ttk.Frame(notebook)
	tab_salir = ttk.Frame(notebook)
	tabla_galeria = crearTabla(tab_galeria,consultarLibros(conn),"Galería")
	tabla_coleccion = crearTablaLista(tab_coleccion,consultarLibrosObtenidos(conn,id_u),"Colección")
	tabla_deseados = crearTablaLista(tab_deseados,consultarLibrosDeseados(conn,id_u),"Deseados")
	tabla_leidos = crearTablaLista(tab_leidos,consultarLibrosLeidos(conn,id_u),"Leídos")
	tabla_galeria.bind('<<TreeviewSelect>>',treeViewListener)
	tabla_coleccion.bind('<<TreeviewSelect>>',treeViewListener)
	tabla_deseados.bind('<<TreeviewSelect>>',treeViewListener)
	tabla_leidos.bind('<<TreeviewSelect>>',treeViewListener)
	notebook.add(tab_galeria, text='Galería')
	notebook.add(tab_coleccion, text='Colección')
	notebook.add(tab_deseados, text='Deseados')
	notebook.add(tab_leidos, text='Leídos')
	notebook.add(tab_salir, text='Salir')
	notebook.grid(row=1,column=0,columnspan=2)	
	notebook.bind('<<NotebookTabChanged>>',tab_switch)
	Button(botonesGenerar).pack()#Error que hace funcionar los botones
def showCrearReporte():
	global reporte
	reporte = Tk()
	centrar(reporte,350,50)
	reporte.resizable(False,False)
	reporte.title("Crear Reporte")
	Label(reporte,text="Nombre del reporte:",anchor=E,width=20).grid(row=0,column=0)
	nombre = Entry(reporte,text="Crear",width=15)
	nombre.grid(row=0,column=1)
	Button(reporte,text="Generar",command=lambda: crearReporte(nombre.get()+".pdf")).grid(row=0,column=2,padx=(10,10),pady=(10,10))
def crearReporte(nombre):
	def grouper(iterable, n):
	    args = [iter(iterable)] * n
	    return itertools.zip_longest(*args)
	global conn, id_user, reporte
	if not(reporte is None):
		try:
			reporte.destroy()
		except:
			pass
	datos = consultarLibrosObtenidos(conn,id_user)
	data = [('Fecha','Titulo','Autor','Edicion','Publicacion','Idioma','Editorial','Año','Saga','Paginas','Capitulos')]
	for row in datos:
		data.append((str(isNone(row[1])),str(isNone(row[2])),str(isNone(row[3])),str(isNone(row[4])),str(isNone(row[5])),str(isNone(row[6])),str(isNone(row[7])),str(isNone(row[8])),str(isNone(row[9])),str(isNone(row[10])),str(isNone(row[11]))))
	c = canvas.Canvas("reportes/"+nombre, pagesize=landscape(A2))
	w, h = landscape(A2)
	max_rows_per_page = 64
	# Margin.
	x_offset = 50
	y_offset = 150
	# Space between rows.
	padding = 15
	xlist = [x + x_offset for x in [0,80,550,790,840,990,1070,1220,1260,1440,1490,1570]]
	ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
	for rows in grouper(data, max_rows_per_page):
	    rows = tuple(filter(bool, rows))
	    c.grid(xlist, ylist[:len(rows) + 1])
	    for y, row in zip(ylist[:-1], rows):
	        for x, cell in zip(xlist, row):
	            c.drawString(x + 2, y - padding + 3, str(cell))
	    c.showPage()

	c.save()
	wb.open_new(os.path.dirname(os.path.abspath(__file__))+"/reportes/"+nombre)
def showOpcionesGrafica():
	global opcionesGraf
	if not(opcionesGraf is None):
		try:
			opcionesGraf.destroy()
		except:
			pass
	opcionesGraf = Tk()
	centrar(opcionesGraf,250,50)
	opcionesGraf.resizable(False,False)
	opcionesGraf.title("Graficar")
	Label(opcionesGraf,text="Graficar por:",anchor=E,width=15).grid(row=0,column=0)
	opcion = ttk.Combobox(opcionesGraf, values=["Año","Mes"],width=4,state="readonly")
	opcion.grid(row=0,column=1)
	opcion.current(0)
	def iniciarGrafica():
		showGrafica(opcion.get())
	Button(opcionesGraf,text="Generar",command=iniciarGrafica).grid(row=0,column=2,padx=(10,10),pady=(10,10))
def showGrafica(modo):
	global notebook, grafica, opcionesGraf,conn,id_user
	if not(opcionesGraf is None):
		try:
			opcionesGraf.destroy()
		except:
			opcionesGraf = None
	if not(grafica is None):
		try:
			grafica.destroy()
		except:
			pass
	grafica = Tk()
	centrar(grafica,800,500)
	grafica.resizable(False,False)
	lista = notebook.tab(notebook.select(), "text")
	title = "Gráfica"
	rows = None
	if modo == "Año":
		title += " por años de "
		if lista ==  "Colección":
			rows = consultarLibrosColeccionPorA(conn,id_user)
		if lista == "Leídos":
			rows = consultarLibrosLeidosPorA(conn,id_user)
	if modo == "Mes":
		title += " por mese de "
		if lista ==  "Colección":
			rows = consultarLibrosColeccionPorMes(conn,id_user)
		if lista == "Leídos":
			rows = consultarLibrosLeidosPorMes(conn,id_user)
	title += lista
	grafica.title(title)
	f = Figure(figsize=(6,4), dpi=100)
	ax = f.add_subplot(111)
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	data = []
	ind = []
	for row in rows:
		ind.append(row[0])
		data.append(row[1])
	ax.set_xticklabels(ind, rotation = 90, ha="right")
	f.tight_layout()
	ax.bar(ind, data)
	canvas = FigureCanvasTkAgg(f, master=grafica)
	#canvas.show()
	canvas.get_tk_widget().pack(expand=1,fill=BOTH)
	print()
def showAdminLista(lista,accion,id_lib):
	global admin, conn, id_user, font
	global btnObtenido,btnDeseado,btnLeido
	if not(admin is None):
		try:
			admin.destroy()
		except:
			pass
		admin = None	
	admin = Tk()
	admin.option_add("*Font",font)
	centrar(admin,400,150) 
	admin.resizable(False, False)
	admin.title(accion+" "+lista)
	datos = consultarLibro(conn,id_lib)[0]
	Label(admin,text="Titulo:",anchor='e',width=8).grid(row=0, column=0)
	Label(admin,text=textwrap.fill(datos[1], width=30),anchor='w',width=30).grid(row=0, column=1)
	Label(admin,text="Fecha:",anchor='e',width=8).grid(row=1, column=0)
	f = None
	if lista == "Colección":
		f = consultarFechaColeccion(conn,id_user,id_lib)
	if lista == "Deseados":
		f = consultarFechaDeseado(conn,id_user,id_lib)
	if lista == "Leídos":
		f = consultarFechaLeido(conn,id_user,id_lib)
	cal = DateEntry(admin,width=11,bg="darkblue",fg="white",locale='es_MX')
	if not(f is None):
		cal.set_date(f)
	cal.grid(row=1, column = 1,sticky='w')
	def agregarLibro(event):
		global conn, id_user
		if lista == "Colección":
			if agregarLibroColeccion(conn,id_user,id_lib,cal.get_date()):
				btnObtenido["text"] = "Editar Colección"
			if True:
				eliminarLibroDeseado(conn,id_user,id_lib)
				btnDeseado['text'] = "Agregar Deseados"
		if lista == "Deseados":
			if agregarLibroDeseado(conn,id_user,id_lib,cal.get_date()):
				btnDeseado["text"] = "Editar Deseados"
		if lista == "Leídos":
			if agregarLibroLeido(conn,id_user,id_lib,cal.get_date()):
				btnLeido["text"] = "Editar Leídos"
		actualizarInformacion()
	def guardarLibro(event):
		if lista == "Colección":
			editarLibroColeccion(conn,id_user,id_lib,cal.get_date())
		if lista == "Deseados":
			editarLibroDeseado(conn,id_user,id_lib,cal.get_date())
		if lista == "Leídos":
			editarLibroLeido(conn,id_user,id_lib,cal.get_date())
		actualizarInformacion()
	def eliminarLibro(event):
		if lista == "Colección":
			if eliminarLibroColeccion(conn,id_user,id_lib):
				btnObtenido["text"] = "Agregar Colección"
		if lista == "Deseados":
			if eliminarLibroDeseado(conn,id_user,id_lib):
				btnDeseado["text"] = "Agregar Deseados"
		if lista == "Leídos":
			if eliminarLibroLeido(conn,id_user,id_lib):
				btnLeido["text"] = "Agregar Leídos"
		actualizarInformacion()
	botones = Frame(admin)
	botones.grid(row=3,column=0, columnspan=2,pady=(10,10))
	btnCancelar = Button(botones,text="Cancelar",command=admin.destroy)
	btnCancelar.grid(row = 0,column=0,padx=(10,10))
	if accion == "Agregar":
		btnAgregar = Button(botones,text="Agregar",command=admin.destroy)
		btnAgregar.bind('<ButtonRelease-1>',agregarLibro)
		btnAgregar.grid(row = 0,column=1,padx=(10,10))
	if accion == "Administrar":
		btnGuardar = Button(botones,text="Guardar",command=admin.destroy)
		btnGuardar.bind('<ButtonRelease-1>',guardarLibro)
		btnGuardar.grid(row = 0,column=1,padx=(10,10))
		btnEliminar = Button(botones,text="Eliminar",command=admin.destroy)
		btnEliminar.bind('<ButtonRelease-1>',eliminarLibro)
		btnEliminar.grid(row = 0,column=2,padx=(10,10))
def showLibro(id_lib):
	global window, conn, id_user, libro, admin, id_libro, font
	global btnObtenido,btnDeseado,btnLeido
	id_libro = id_lib
	if not(admin is None):
		try:
			admin.destroy()
		except:
			pass
	if not(libro is None):
		try:
			libro.destroy()
		except:
			pass
		libro = None
	libro = Tk()
	libro.option_add("*Font",font)
	libro.protocol("WM_DELETE_WINDOW", cerrarAdmin)
	centrar(libro,850,450) 
	libro.resizable(False, False)
	libro.title("Libro")
	botones = Frame(libro)
	def adminLista(event):
		global libro
		btn = event.widget
		lis = ""
		accion = ""
		if "Agregar" in btn['text']:
			accion = "Agregar"
		if "Editar" in btn['text']:
			accion = "Administrar"
		if "Colección" in btn['text']:
			lis = "Colección"
		if "Deseados" in btn['text']:
			lis = "Deseados"
		if "Leídos" in btn['text']:
			lis = "Leídos"
		if accion == "Agregar" and lis == "Deseados":
			if isLibroColeccion(conn,id_user,id_lib):
				messagebox.showinfo("Info Existencia", "Ya tienes este libro en tu Colección")
				libro.lift()
				return
		showAdminLista(lis,accion,id_lib)
	if isLibroColeccion(conn, id_user,id_lib):
		btnObtenido = Button(botones,text="Editar Colección")
	else:
		btnObtenido = Button(botones,text="Agregar Colección")
	if isLibroDeseado(conn, id_user,id_lib):
		btnDeseado = Button(botones,text="Editar Deseados")
	else:
		btnDeseado = Button(botones,text="Agregar Deseados")
	if isLibroLeido(conn, id_user,id_lib):
		btnLeido = Button(botones,text="Editar Leídos")
	else:
		btnLeido = Button(botones,text="Agregar Leídos")
	btnObtenido.bind('<ButtonRelease-1>',adminLista)
	btnDeseado.bind('<ButtonRelease-1>',adminLista)
	btnLeido.bind('<ButtonRelease-1>',adminLista)
	btnObtenido.grid(row=0,pady=(10,10))
	btnDeseado.grid(row=1,pady=(10,10))
	btnLeido.grid(row=2,pady=(10,10))
	Label(libro,text="Titulo:",anchor="e",width=12).grid(row=0, column=0,padx=(10,10))
	Label(libro,text="Autor:",anchor="e",width=12).grid(row=1, column=0,padx=(10,10))
	Label(libro,text="Edicion:",anchor="e",width=12).grid(row=2, column=0,padx=(10,10))
	Label(libro,text="Publicacion:",anchor="e",width=12).grid(row=3, column=0,padx=(10,10))
	Label(libro,text="Idioma:",anchor="e",width=12).grid(row=4, column=0,padx=(10,10))
	Label(libro,text="Editorial:",anchor="e",width=12).grid(row=5, column=0,padx=(10,10))
	Label(libro,text="Año:",anchor="e",width=12).grid(row=6, column=0,padx=(10,10))
	Label(libro,text="Saga:",anchor="e",width=12).grid(row=7, column=0,padx=(10,10))
	Label(libro,text="Paginas:",anchor="e",width=12).grid(row=8, column=0,padx=(10,10))
	Label(libro,text="Capitulos:",anchor="e",width=12).grid(row=9, column=0,padx=(10,10))
	Label(libro,text="Sinopsis:",anchor="e",width=12).grid(row=10, column=0,padx=(10,10))
	def acomodarSaltosLinea(text,characters):
		if text is None:
			return ""
		return textwrap.fill(text, width=characters)
	datos = consultarLibro(conn,id_libro)[0]
	Label(libro,text=acomodarSaltosLinea(datos[1],50),anchor="w",width=50).grid(row=0, column=1)
	Label(libro,text=datos[2],anchor="w",width=50).grid(row=1, column=1)
	Label(libro,text=datos[3],anchor="w",width=50).grid(row=2, column=1)
	Label(libro,text=datos[4],anchor="w",width=50).grid(row=3, column=1)
	Label(libro,text=datos[5],anchor="w",width=50).grid(row=4, column=1)
	Label(libro,text=datos[6],anchor="w",width=50).grid(row=5, column=1)
	Label(libro,text=datos[7],anchor="w",width=50).grid(row=6, column=1)
	Label(libro,text=datos[8],anchor="w",width=50).grid(row=7, column=1)
	Label(libro,text=datos[9],anchor="w",width=50).grid(row=8, column=1)
	Label(libro,text=datos[10],anchor="w",width=50).grid(row=9, column=1)
	sinopsis = ScrolledText(libro, width=48,height=8)
	sinopsis.insert("1.0", acomodarSaltosLinea(datos[11],35))
	sinopsis.config(state=DISABLED)
	sinopsis.grid(row=10, column=1)
	botones.grid(row=0,column=2,rowspan=11)
def showLogin():	
	global window, login, register, conn, id_user, font

	if not(register is None):
		register.destroy()
		register = None
	destroyAll()
	login = Tk()
	login.option_add("*Font",font)
	centrar(login,510,199) 
	login.resizable(False, False)
	login.title("Inicio de Sesión")
	img = PhotoImage(file="img/librero.gif")
	img = img.subsample(2, 2)
	Label(login,image=img,bd=0).grid(row=0,column=0,rowspan=3)
	Label(login,image=img,bd=0).grid(row=0,column=3,rowspan=3)
	Label(login, text="Usuario:",anchor="e",width=12).grid(row=0, column=1)
	username = StringVar()
	Entry(login, textvariable=username).grid(row=0, column=2,padx=(10,40))  
	Label(login,text="Contraseña:",anchor="e",width=12).grid(row=1, column=1)  
	password = StringVar()
	Entry(login, textvariable=password, show='*').grid(row=1, column=2,padx=(10,40))
	def btnIniciarSesion():
		if validarDatosInicioSesion(username.get(),password.get()):
			id_u = iniciarSesion(conn,username.get(),password.get())
			if not(id_u is None):
				iniciarApp(id_u)
			else:
				messagebox.showerror("Error", "Usuario o Contraseña Incorrectos")
	botones = Frame(login)
	botones.grid(row=2,column=1,columnspan=2,pady=(10,10))
	Button(botones, text="Registrar", command=showRegister,width=10).grid(row=0, column=0,padx=(10,10)) 
	Button(botones, text="Iniciar", command=btnIniciarSesion,width=10).grid(row=0, column=1,padx=(10,10)) 
	login.mainloop()

def showRegister():
	global login, register, conn, id_user, font
	if not(login is None):
		login.destroy()
		login = None
	register = Tk()
	register.option_add("*Font",font)
	centrar(register,715,390)
	register.resizable(False, False)
	register.title("Registro")
	img = PhotoImage(file="img/librero.gif")
	Label(login,image=img,bd=0).grid(row=0,column=0,rowspan=7)
	Label(login,image=img,bd=0).grid(row=0,column=3,rowspan=7)
	
	Label(register, text="Nombre:",anchor="e",width=19).grid(row=0, column=1)
	nombre = StringVar()
	Entry(register, textvariable=nombre).grid(row=0, column=2,padx=(10,40))
	Label(register,text="Primer Apellido:",anchor="e",width=19).grid(row=1, column=1)  
	primerApe = StringVar()
	Entry(register, textvariable=primerApe).grid(row=1, column=2,padx=(10,40))
	Label(register,text="Segundo Apellido:",anchor="e",width=19).grid(row=2, column=1)  
	segundoApe = StringVar()
	Entry(register, textvariable=segundoApe).grid(row=2, column=2,padx=(10,40))
	Label(register, text="Usuario:",anchor="e",width=19).grid(row=3, column=1)
	username = StringVar()	
	Entry(register, textvariable=username).grid(row=3, column=2,padx=(10,40))
	Label(register,text="Contraseña:",anchor="e",width=19).grid(row=4, column=1)  
	password = StringVar()
	Entry(register, textvariable=password, show='*').grid(row=4, column=2,padx=(10,40))
	Label(register,text="Confirma Contraseña:",anchor="e",width=19).grid(row=5, column=1)  
	repassword = StringVar()
	Entry(register, textvariable=repassword, show='*').grid(row=5, column=2,padx=(10,40))
	def btnRegistrarUsuario():
		if validarDatosRegistro(nombre.get(),primerApe.get(),segundoApe.get(),username.get(),password.get(),repassword.get()):
			if registrarUsuario(conn, nombre.get(),primerApe.get(),segundoApe.get(),username.get(),password.get()):
				id_u = iniciarSesion(conn, username.get(),password.get())
				iniciarApp(id_u)
	botones = Frame(register)
	botones.grid(row=6,column=1,columnspan=2,pady=(10,10))
	Button(botones, text="Cancelar", command=showLogin).grid(row=6, column=0,padx=(10,10)) 
	Button(botones, text="Register", command=btnRegistrarUsuario).grid(row=6, column=1,padx=(10,10)) 
	register.mainloop()
def centrar(window,width, height):
	window.geometry("{}x{}+{}+{}".format(width,height,int(window.winfo_screenwidth()/2 - width/2),int(window.winfo_screenheight()/2 - height/2)))
if(conn.db):
	print("Conectado")
	showLogin()
else:
	messagebox.showerror("Error BD", "Fallo en la conexión a la BD")
