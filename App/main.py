from tkinter import *				
from tkinter import messagebox
from tkinter import ttk
from connection import *
from validacion import *
from tabFrames import *
from libros import *
from usuarios import *
import textwrap
from tkinter.scrolledtext import *
from tkcalendar import *
from datetime import *
window = register = login = libro = admin =None
notebook = None
tabla_galeria = tabla_coleccion = tabla_deseados = tabla_leidos = None
id_user = id_libro = None
usuarioColecValue = usuarioDeseadValue = usuarioLeidosValue = infousuario = None
btnObtenido = btnDeseado = btnLeido = None
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
	global window, register, login, id_user
	id_user = id_u
	if not(register is None):
		register.destroy()
		register = None
	if not(login is None):
		login.destroy()
		login = None
	window = Tk()
	centrar(window,1000,700) 
	window.resizable(False, False)
	window.title('My Book Collection')
	informacionUsuario(id_u)
	menuprincipal(id_u)
	window.protocol("WM_DELETE_WINDOW", destroyAll)
	window.mainloop()
def tab_switch(event):
	global tabla_galeria, conn
	if notebook.tab(notebook.select(), "text") == "Salir":
		id_user = None
		showLogin()
	actualizarInformacion()
def actualizarInformacion():
	global tabla_galeria, tabla_coleccion, tabla_deseados, tabla_leidos, id_user
	actualizarTabla(tabla_galeria,consultarLibros(conn))
	actualizarTabla(tabla_coleccion,consultarLibrosObtenidos(conn,id_user))
	actualizarTabla(tabla_deseados,consultarLibrosDeseados(conn,id_user))
	actualizarTabla(tabla_leidos,consultarLibrosLeidos(conn,id_user))
	actualizarCantidades()
def informacionUsuario(id_u):
	global usuarioColecValue, usuarioDeseadValue, usuarioLeidosValue, infousuario, id_user
	infousuario = Frame(window)
	infousuario.pack(side = TOP)
	usuarioLabel = Label(infousuario,text="Usuario:").grid(row=0, column=0)  
	usuarioColecLabel = Label(infousuario,text="Libros Obtenidos:").grid(row=1, column=0)  
	usuarioDeseadLabel = Label(infousuario,text="Libros Deseados:").grid(row=1, column=2)  
	usuarioLeidosLabel = Label(infousuario,text="Libros Leidos:").grid(row=1, column=4)  
	usuarioValue = Label(infousuario,text=consultarNombre(conn,id_u)).grid(row=0, column=1, columnspan=4)
	actualizarCantidades()
def treeViewListener(event):
	tree = event.widget
	showLibro(tree.item(tree.selection(),'text'))
def actualizarCantidades():
	global usuarioColecValue, usuarioDeseadValue, usuarioLeidosValue, infousuario, id_user
	usuarioColecValue = Label(infousuario,text=cantidadLibrosObtenidos(conn,id_user)).grid(row=1, column=1)
	usuarioDeseadValue = Label(infousuario,text=cantidadLibrosDeseados(conn,id_user)).grid(row=1, column=3)
	usuarioLeidosValue = Label(infousuario,text=cantidadLibrosLeidos(conn,id_user)).grid(row=1, column=5)
def menuprincipal(id_u):
	global notebook, conn, tabla_galeria, tabla_coleccion, tabla_deseados, tabla_leidos
	style = ttk.Style(window)
	style.configure('lefttab.TNotebook', tabposition='ws')
	style.configure('lefttab.TNotebook.Tab', margin = 10, padding = [10,20])
	notebook = ttk.Notebook(window, style='lefttab.TNotebook')	
	tab_galeria = ttk.Frame(notebook)
	tab_coleccion = ttk.Frame(notebook)
	tab_deseados = ttk.Frame(notebook)
	tab_leidos = ttk.Frame(notebook)
	tab_salir = ttk.Frame(notebook)
	tabla_galeria = crearTabla(tab_galeria,consultarLibros(conn),"Galería")
	tabla_coleccion = crearTabla(tab_coleccion,consultarLibrosObtenidos(conn,id_u),"Colección")
	tabla_deseados = crearTabla(tab_deseados,consultarLibrosDeseados(conn,id_u),"Deseados")
	tabla_leidos = crearTabla(tab_leidos,consultarLibrosLeidos(conn,id_u),"Leídos")
	tabla_galeria.bind('<<TreeviewSelect>>',treeViewListener)
	tabla_coleccion.bind('<<TreeviewSelect>>',treeViewListener)
	tabla_deseados.bind('<<TreeviewSelect>>',treeViewListener)
	tabla_leidos.bind('<<TreeviewSelect>>',treeViewListener)
	notebook.add(tab_galeria, text='Galería')
	notebook.add(tab_coleccion, text='Coleccion')
	notebook.add(tab_deseados, text='Deseados')
	notebook.add(tab_leidos, text='Leídos')
	notebook.add(tab_salir, text='Salir')
	notebook.pack(expand=1, fill='both')	
	notebook.bind('<ButtonRelease-1>',tab_switch)
def showAdminLista(lista,accion,id_lib):
	global admin, id_libro
	global btnObtenido,btnDeseado,btnLeido
	if not(admin is None):
		try:
			admin.destroy()
		except:
			pass
		admin = None	
	admin = Tk()
	centrar(admin,300,200) 
	admin.resizable(False, False)
	admin.title(accion+" "+lista)
	datos = consultarLibro(conn,id_libro)[0]
	Label(admin,text="Titulo: ").grid(row=0, column=0)
	Label(admin,text=datos[1]).grid(row=0, column=1)
	Label(admin,text="Fecha: ").grid(row=1, column=0)
	cal = DateEntry(admin,width=30,bg="darkblue",fg="white",locale='es_MX')
	cal.grid(row=1, column = 1)
	print()
	def agregarLibro(event):
		global conn, id_user
		if lista == "Coleccion":
			if agregarLibroColeccion(conn,id_user,id_lib,cal.get_date()):
				btnObtenido["text"] = "Editar Coleccion"
			if True:
				eliminarLibroDeseado(conn,id_user,id_lib)
				btnDeseado['text'] = "Agregar Deseados"
		if lista == "Deseados":
			btnDeseado["text"] = "Editar Deseados"
		if lista == "Leidos":
			btnLeido["text"] = "Editar Leidos"
		actualizarInformacion()
	botones = Frame(admin)
	botones.grid(row=3,column=0, columnspan=2)
	btnCancelar = Button(botones,text="Cancelar",command=admin.destroy)
	btnCancelar.grid(row = 0,column=0)
	print(accion == "Agregar")
	if accion == "Agregar":
		btnAgregar = Button(botones,text="Agregar",command=admin.destroy)
		btnAgregar.bind('<ButtonRelease-1>',agregarLibro)
		btnAgregar.grid(row = 0,column=1)
	if accion == "Administrar":
		pass
def showLibro(id_lib):
	global window, conn, id_user, libro, admin, id_libro
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
	libro.protocol("WM_DELETE_WINDOW", cerrarAdmin)
	centrar(libro,550,400) 
	libro.resizable(False, False)
	libro.title("Libro")
	botones = Frame(libro)
	def adminLista(event):
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
		showAdminLista(lis,accion,id_lib)
	btnObtenido = Button(botones,text="Agregar Coleccion")
	btnDeseado = Button(botones,text="Agregar Deseados")
	btnLeido = Button(botones,text="Agregar Leidos")
	btnObtenido.bind('<ButtonRelease-1>',adminLista)
	btnDeseado.bind('<ButtonRelease-1>',adminLista)
	btnLeido.bind('<ButtonRelease-1>',adminLista)
	btnObtenido.grid(row=0)
	btnDeseado.grid(row=1)
	btnLeido.grid(row=2)
	Label(libro,text="Titulo: ").grid(row=0, column=0)
	Label(libro,text="Autor: ").grid(row=1, column=0)
	Label(libro,text="Edicion: ").grid(row=2, column=0)
	Label(libro,text="Publicacion: ").grid(row=3, column=0)
	Label(libro,text="Idioma: ").grid(row=4, column=0)
	Label(libro,text="Editorial: ").grid(row=5, column=0)
	Label(libro,text="Año: ").grid(row=6, column=0)
	Label(libro,text="Saga: ").grid(row=7, column=0)
	Label(libro,text="Paginas: ").grid(row=8, column=0)
	Label(libro,text="Capitulos: ").grid(row=9, column=0)
	Label(libro,text="Sinopsis: ").grid(row=10, column=0)
	def acomodarSaltosLinea(text,characters):
		if text is None:
			return ""
		return textwrap.fill(text, width=characters)
	datos = consultarLibro(conn,id_libro)[0]
	Label(libro,text=acomodarSaltosLinea(datos[1],50)).grid(row=0, column=1)
	Label(libro,text=datos[2]).grid(row=1, column=1)
	Label(libro,text=datos[3]).grid(row=2, column=1)
	Label(libro,text=datos[4]).grid(row=3, column=1)
	Label(libro,text=datos[5]).grid(row=4, column=1)
	Label(libro,text=datos[6]).grid(row=5, column=1)
	Label(libro,text=datos[7]).grid(row=6, column=1)
	Label(libro,text=datos[8]).grid(row=7, column=1)
	Label(libro,text=datos[9]).grid(row=8, column=1)
	Label(libro,text=datos[10]).grid(row=9, column=1)
	sinopsis = ScrolledText(libro, width=40,height=8)
	sinopsis.insert("1.0", acomodarSaltosLinea(datos[11],35))
	sinopsis.config(state=DISABLED)
	sinopsis.grid(row=10, column=1)
	botones.grid(row=0,column=2,rowspan=11)
def showLogin():	
	global window, login, register, conn, id_user
	if not(register is None):
		register.destroy()
		register = None
	if not(window is None):
		window.destroy()
		window = None
	login = Tk()
	centrar(login,200,80) 
	login.resizable(False, False)
	login.title("Login")	
	usernameLabel = Label(login, text="Usuario").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(login, textvariable=username).grid(row=0, column=1)  
	passwordLabel = Label(login,text="Contraseña").grid(row=1, column=0)  
	password = StringVar()
	passwordEntry = Entry(login, textvariable=password, show='*').grid(row=1, column=1)
	def btnIniciarSesion():
		if validarDatosInicioSesion(username.get(),password.get()):
			id_u = iniciarSesion(conn,username.get(),password.get())
			if not(id_u is None):
				iniciarApp(id_u)
			else:
				messagebox.showerror("Error", "Usuario o Contraseña Incorrectos")
	registerButton = Button(login, text="Register", command=showRegister).grid(row=2, column=0,sticky=W+E) 
	loginButton = Button(login, text="Login", command=btnIniciarSesion).grid(row=2, column=1,sticky=W+E) 
	login.mainloop()

def showRegister():
	global login, register, conn, id_user
	if not(login is None):
		login.destroy()
		login = None
	register = Tk()
	centrar(register,260,170)
	register.resizable(False, False)
	register.title("Registro")
	nombreEtiqueta = Label(register, text="Nombre").grid(row=0, column=0)
	nombre = StringVar()
	nombreEntry = Entry(register, textvariable=nombre).grid(row=0, column=1)  
	primerApeEtiqueta = Label(register,text="Primer Apellido").grid(row=1, column=0)  
	primerApe = StringVar()
	primerApeEntry = Entry(register, textvariable=primerApe).grid(row=1, column=1)
	segundoApeEtiqueta = Label(register,text="Segundo Apellido").grid(row=2, column=0)  
	segundoApe = StringVar()
	segundoApeEntry = Entry(register, textvariable=segundoApe).grid(row=2, column=1)
	usernameLabel = Label(register, text="Usuario").grid(row=3, column=0)
	username = StringVar()	
	usernameEntry = Entry(register, textvariable=username).grid(row=3, column=1)  
	passwordLabel = Label(register,text="Contraseña").grid(row=4, column=0)  
	password = StringVar()
	passwordEntry = Entry(register, textvariable=password, show='*').grid(row=4, column=1)
	repasswordLabel = Label(register,text="Confirma Contraseña").grid(row=5, column=0)  
	repassword = StringVar()
	repasswordEntry = Entry(register, textvariable=repassword, show='*').grid(row=5, column=1)
	def btnRegistrarUsuario():
		if validarDatosRegistro(nombre.get(),primerApe.get(),segundoApe.get(),username.get(),password.get(),repassword.get()):
			if registrarUsuario(conn, nombre.get(),primerApe.get(),segundoApe.get(),username.get(),password.get()):
				id_u = iniciarSesion(conn, username.get(),password.get())
				iniciarApp(id_u)
	cancelButton = Button(register, text="Cancelar", command=showLogin).grid(row=6, column=0,sticky=W+E) 
	registrarButton = Button(register, text="Register", command=btnRegistrarUsuario).grid(row=6, column=1,sticky=W+E) 
	register.mainloop()
def centrar(window,width, height):
	window.geometry("{}x{}+{}+{}".format(width,height,int(window.winfo_screenwidth()/2 - width/2),int(window.winfo_screenheight()/2 - height/2)))
if(conn.db):
	print("Conectado")
	showLogin()
else:
	messagebox.showerror("Error BD", "Fallo en la conexión a la BD")
