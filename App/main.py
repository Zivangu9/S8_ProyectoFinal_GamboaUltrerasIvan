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
font =("Bookman Old Style", 12)
window = register = login = libro = admin =None
notebook = None
tabla_galeria = tabla_coleccion = tabla_deseados = tabla_leidos = None
id_user = id_libro = None
usuarioColecValue = usuarioDeseadValue = usuarioLeidosValue = infousuario = None
btnObtenido = btnDeseado = btnLeido = None
btnGrafica = btnReporte = None
conn = Connection()
def destroyAll():
	global window, register, login, libro, admin
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
	centrar(window,1000,700) 
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
	nombreFrame.grid(row=0,columnspan=6)
	usuarioLabel = Label(nombreFrame,text="Usuario:",anchor="e",width=12).grid(row=0, column=0)  
	usuarioColecLabel = Label(infousuario,text="Libros Obtenidos:",anchor="e",width=15).grid(row=1, column=0)  
	usuarioDeseadLabel = Label(infousuario,text="Libros Deseados:",anchor="e",width=17).grid(row=1, column=2)  
	usuarioLeidosLabel = Label(infousuario,text="Libros Leidos:",anchor="e",width=15).grid(row=1, column=4)  
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
	def crearGrafica():
		print("Graficando")
	def crearReporte():
		print("Reportando")
	botonesGenerar = Frame(window,width=193, height = 106)
	botonesGenerar.grid(row=0,column=1)
	iconGrafica = PhotoImage(file="img/grafica.png")
	iconGrafica = iconGrafica.subsample(10, 10)
	btnGrafica = Button(botonesGenerar,text = "Graficar",image=iconGrafica,compound=TOP,command=crearGrafica)
	btnGrafica.grid(row=0,column=0,padx=(10,10),pady=(10,10))
	iconReporte = PhotoImage(file="img/reporte.png")
	iconReporte = iconReporte.subsample(10, 10)
	btnReporte = Button(botonesGenerar,text = "Reporte",image=iconReporte,compound=TOP,command=crearReporte)
	btnReporte.grid(row=0,column=1,padx=(10,10),pady=(10,10))
	style = ttk.Style(window)
	style.configure('lefttab.TNotebook', tabposition='ws')
	style.configure('lefttab.TNotebook.Tab', margin = 10, padding = [10,20])
	notebook = ttk.Notebook(window, style='lefttab.TNotebook',width=900,height=500)
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
	notebook.add(tab_coleccion, text='Coleccion')
	notebook.add(tab_deseados, text='Deseados')
	notebook.add(tab_leidos, text='Leídos')
	notebook.add(tab_salir, text='Salir')
	notebook.grid(row=1,column=0,columnspan=2)	
	notebook.bind('<<NotebookTabChanged>>',tab_switch)
	Button(botonesGenerar).pack()#Error que hace funcionar los botones
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
	if lista == "Coleccion":
		f = consultarFechaColeccion(conn,id_user,id_lib)
	if lista == "Deseados":
		f = consultarFechaDeseado(conn,id_user,id_lib)
	if lista == "Leidos":
		f = consultarFechaLeido(conn,id_user,id_lib)
	cal = DateEntry(admin,width=11,bg="darkblue",fg="white",locale='es_MX')
	if not(f is None):
		cal.set_date(f)
	cal.grid(row=1, column = 1,sticky='w')
	def agregarLibro(event):
		global conn, id_user
		if lista == "Coleccion":
			if agregarLibroColeccion(conn,id_user,id_lib,cal.get_date()):
				btnObtenido["text"] = "Editar Coleccion"
			if True:
				eliminarLibroDeseado(conn,id_user,id_lib)
				btnDeseado['text'] = "Agregar Deseados"
		if lista == "Deseados":
			if agregarLibroDeseado(conn,id_user,id_lib,cal.get_date()):
				btnDeseado["text"] = "Editar Deseados"
		if lista == "Leidos":
			if agregarLibroLeido(conn,id_user,id_lib,cal.get_date()):
				btnLeido["text"] = "Editar Leidos"
		actualizarInformacion()
	def guardarLibro(event):
		if lista == "Coleccion":
			editarLibroColeccion(conn,id_user,id_lib,cal.get_date())
		if lista == "Deseados":
			editarLibroDeseado(conn,id_user,id_lib,cal.get_date())
		if lista == "Leidos":
			editarLibroLeido(conn,id_user,id_lib,cal.get_date())
		actualizarInformacion()
	def eliminarLibro(event):
		if lista == "Coleccion":
			if eliminarLibroColeccion(conn,id_user,id_lib):
				btnObtenido["text"] = "Agregar Coleccion"
		if lista == "Deseados":
			if eliminarLibroDeseado(conn,id_user,id_lib):
				btnDeseado["text"] = "Agregar Deseados"
		if lista == "Leidos":
			if eliminarLibroLeido(conn,id_user,id_lib):
				btnLeido["text"] = "Agregar Leidos"
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
		if "Coleccion" in btn['text']:
			lis = "Coleccion"
		if "Deseados" in btn['text']:
			lis = "Deseados"
		if "Leidos" in btn['text']:
			lis = "Leidos"
		if accion == "Agregar" and lis == "Deseados":
			if isLibroColeccion(conn,id_user,id_lib):
				messagebox.showinfo("Info Existencia", "Ya tienes este libro en tu Colección")
				libro.lift()
				return
		showAdminLista(lis,accion,id_lib)
	if isLibroColeccion(conn, id_user,id_lib):
		btnObtenido = Button(botones,text="Editar Coleccion")
	else:
		btnObtenido = Button(botones,text="Agregar Coleccion")
	if isLibroDeseado(conn, id_user,id_lib):
		btnDeseado = Button(botones,text="Editar Deseados")
	else:
		btnDeseado = Button(botones,text="Agregar Deseados")
	if isLibroLeido(conn, id_user,id_lib):
		btnLeido = Button(botones,text="Editar Leidos")
	else:
		btnLeido = Button(botones,text="Agregar Leidos")
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
	if not(window is None):
		window.destroy()
		window = None
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
