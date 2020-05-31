from tkinter import *				
from tkinter import messagebox
from tkinter import ttk
from connection import *
from validacion import *
from tabFrames import *
from libros import *
from usuarios import *
window = register = login = None
notebook = None
tabla_galeria = tabla_coleccion = tabla_deseados = tabla_leidos = None
id_user = None
usuarioColecValue = usuarioDeseadValue = usuarioLeidosValue = infousuario = None
conn = Connection()
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
	centrar(window,600,700) 
	window.resizable(False, False)
	window.title('My Book Collection')
	informacionUsuario(id_u)
	menuprincipal(id_u)
	window.mainloop()
def tab_switch(event):
	global tabla_galeria, conn
	if notebook.tab(notebook.select(), "text") == "Salir":
		id_user = None
		showLogin()
	if notebook.tab(notebook.select(), "text") == "Galeria":
		actualizarTabla(tabla_galeria,consultarLibros(conn))
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
		
def actualizarCantidades():
	global usuarioColecValue, usuarioDeseadValue, usuarioLeidosValue, infousuario, id_user
	usuarioColecValue = Label(infousuario,text=cantidadLibrosObtenidos(conn,id_user)).grid(row=1, column=1)
	usuarioDeseadValue = Label(infousuario,text=cantidadLibrosDeseados(conn,id_user)).grid(row=1, column=3)
	usuarioLeidosValue = Label(infousuario,text=cantidadLibrosLeidos(conn,id_user)).grid(row=1, column=5)
def menuprincipal(id_u):
	global notebook, conn, tabla_galeria
	style = ttk.Style(window)
	style.configure('lefttab.TNotebook', tabposition='ws')
	style.configure('lefttab.TNotebook.Tab', margin = 10, padding = [10,20])
	notebook = ttk.Notebook(window, style='lefttab.TNotebook')	
	tab_galeria = ttk.Frame(notebook)
	tab_coleccion = ttk.Frame(notebook)
	tab_deseados = ttk.Frame(notebook)
	tab_leidos = ttk.Frame(notebook)
	tab_salir = ttk.Frame(notebook)
	tabla_galeria = crearTabla(tab_galeria,consultarLibros(conn),"Galeria")
	tabla_coleccion = crearTabla(tab_coleccion,consultarLibrosObtenidos(conn,id_u),"Colección")
	tabla_deseados = crearTabla(tab_deseados,consultarLibrosDeseados(conn,id_u),"Deseados")
	tabla_leidos = crearTabla(tab_leidos,consultarLibros(conn),"Leidos")
	notebook.add(tab_galeria, text='Galeria')
	notebook.add(tab_coleccion, text='Coleccion')
	notebook.add(tab_deseados, text='Deseados')
	notebook.add(tab_leidos, text='Leidos')
	notebook.add(tab_salir, text='Salir')
	notebook.pack(expand=1, fill='both')	
	notebook.bind('<ButtonRelease-1>',tab_switch)

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
	usernameLabel = Label(register, text="Usuairo").grid(row=3, column=0)
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
