from tkinter import *				
from tkinter import messagebox
from tkinter import ttk
from connection import *
from validacion import *
from tabFrames import *
from libros import *
window = register = login = None
notebook = None
tabla_galeria = None
conn = Connection()
def iniciarApp(nombre):
	global window, register, login
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
	menuprincipal()
	window.mainloop()
def tab_switch(event):
	global tabla_galeria, conn
	if notebook.tab(notebook.select(), "text") == "Salir":
		showLogin()
	if notebook.tab(notebook.select(), "text") == "Galeria":
		actualizarTabla(tabla_galeria,consultarLibros(conn))
		#notebook.tab(notebook.select()).update()
def menuprincipal():
	global notebook, conn, tabla_galeria
	style = ttk.Style(window)
	style.configure('lefttab.TNotebook', tabposition='ws')
	style.configure('lefttab.TNotebook.Tab', margin = 10, padding = [10,20])
	notebook = ttk.Notebook(window, style='lefttab.TNotebook')	
	tab_galeria = ttk.Frame(notebook)
	tabla_galeria = crearTabla(tab_galeria,consultarLibros(conn))
	tab_coleccion = ttk.Frame(notebook)
	tab_deseados = ttk.Frame(notebook)
	tab_leidos = ttk.Frame(notebook)
	tab_salir = ttk.Frame(notebook,)
	notebook.add(tab_galeria, text='Galeria')
	notebook.add(tab_coleccion, text='Coleccion')
	notebook.add(tab_deseados, text='Deseados')
	notebook.add(tab_leidos, text='Leidos')
	notebook.add(tab_salir, text='Salir')
	notebook.pack(expand=1, fill='both')	
	notebook.bind('<ButtonRelease-1>',tab_switch)

def showLogin():	
	global window, login, register, conn
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
	def iniciarSesion():
		sql_select_query = """ SELECT * FROM usuario WHERE usuario = %s AND clave = SHA1(%s)"""
		if validarInicioSesion(username.get(),password.get()):
			conn.cursor.execute(sql_select_query,(username.get(),password.get()))
			rows = conn.cursor.fetchall()		
			if (len(rows)==1):
				nom = rows[0][1],rows[0][2],rows[0][3]
				iniciarApp(nom)
			else:
				messagebox.showerror("Error", "Usuario o Contraseña Incorrectos")
	registerButton = Button(login, text="Register", command=showRegister).grid(row=2, column=0,sticky=W+E) 
	loginButton = Button(login, text="Login", command=iniciarSesion).grid(row=2, column=1,sticky=W+E) 
	login.mainloop()

def showRegister():
	global login, register, conn
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

	def registrarUsuario():
		sql_insert_query = """INSERT INTO usuario(nombre,primer_apellido,segundo_apellido,usuario,clave) VALUES(%s,%s,%s,%s,SHA1(%s))"""
		if validarRegistro(nombre.get(),primerApe.get(),segundoApe.get(),username.get(),password.get(),repassword.get()):
			try:
				conn.cursor.execute(sql_insert_query,(nombre.get(),primerApe.get(),segundoApe.get(),username.get(),password.get()))
				conn.db.commit()
				nom = nombre.get(),primerApe.get(),segundoApe.get();
				iniciarApp(nom)
			except:
				messagebox.showerror("Error Usuario", "Ese Usuario ya existe")
				do.rollback()	
	cancelButton = Button(register, text="Cancelar", command=showLogin).grid(row=6, column=0,sticky=W+E) 
	registrarButton = Button(register, text="Register", command=registrarUsuario).grid(row=6, column=1,sticky=W+E) 
	register.mainloop()
def centrar(window,width, height):
	window.geometry("{}x{}+{}+{}".format(width,height,int(window.winfo_screenwidth()/2 - width/2),int(window.winfo_screenheight()/2 - height/2)))
if(conn.db):
	print("Conectado")
	showLogin()
else:
	messagebox.showerror("Error BD", "Fallo en la conexión a la BD")
