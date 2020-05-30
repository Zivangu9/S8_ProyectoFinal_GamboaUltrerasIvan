from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from connection import *
window = register = login = None
conn = Connection()
def iniciarApp():
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
	window.title("My Book Collection")
	menuprincipal()
	window.mainloop()
def menuprincipal():
	pass	
def showLogin():
	global login, register, conn
	if not(register is None):
		register.destroy()
		register = None
	login = Tk()
	centrar(login,200,100) 
	login.resizable(False, False)
	login.title("Login")
	usernameLabel = Label(login, text="User Name").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(login, textvariable=username).grid(row=0, column=1)  
	passwordLabel = Label(login,text="Password").grid(row=1, column=0)  
	password = StringVar()
	passwordEntry = Entry(login, textvariable=password, show='*').grid(row=1, column=1)
	def validateLogin():
		sql_select_query = """ SELECT * FROM usuario WHERE usuario = %s AND clave = SHA1(%s)"""
		conn.cursor.execute(sql_select_query,(username.get(),password.get()))
		rows = conn.cursor.fetchall()
		if (len(rows)==1):
			iniciarApp()
		else:
			messagebox.showerror("Error", "Usuario o Contraseña Incorrectos")
	registerButton = Button(login, text="Register", command=showRegister).grid(row=2, column=0,sticky=W+E) 
	loginButton = Button(login, text="Login", command=validateLogin).grid(row=2, column=1,sticky=W+E) 
	login.mainloop()
def showRegister():
	global login
	global register
	if not(login is None):
		login.destroy()
		login = None
	register = Tk()
	centrar(register,200,100)
	register.resizable(False, False)
	register.title("Registro")
	usernameLabel = Label(register, text="User Name").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(register, textvariable=username).grid(row=0, column=1)  
	passwordLabel = Label(register,text="Password").grid(row=1, column=0)  
	password = StringVar()
	passwordEntry = Entry(register, textvariable=password, show='*').grid(row=1, column=1)
	passwordLabel = Label(register,text="Repeat Password").grid(row=1, column=0)  
	repassword = StringVar()
	passwordEntry = Entry(register, textvariable=repassword, show='*').grid(row=1, column=1)

	def validateRegister():
		if (True):
			iniciarApp()
		pass
	cancelButton = Button(register, text="Cancelar", command=showLogin).grid(row=2, column=0,sticky=W+E) 
	registrarButton = Button(register, text="Register", command=validateRegister).grid(row=2, column=1,sticky=W+E) 
	register.mainloop()
def centrar(window,width, height):
	window.geometry("{}x{}+{}+{}".format(width,height,int(window.winfo_screenwidth()/2 - width/2),int(window.winfo_screenheight()/2 - height/2)))
if(conn.db):
	print("Conectado")
	showLogin()
else:
	messagebox.showerror("Error", "Fallo en la conexión a la BD")
