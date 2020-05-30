from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window = None
login = Tk()
def iniciarApp():
	login.destroy()
	window = Tk()
	window.geometry('600x700') 
	window.resizable(False, False)
	window.title("My Book Collection")
	menuprincipal()
	window.mainloop()
def menuprincipal():
	pass	
def showLogin():
	login.geometry('400x400') 
	login.resizable(False, False)
	login.title("Login")
	usernameLabel = Label(login, text="User Name").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(login, textvariable=username).grid(row=0, column=1)  
	passwordLabel = Label(login,text="Password").grid(row=1, column=0)  
	password = StringVar()
	passwordEntry = Entry(login, textvariable=password, show='*').grid(row=1, column=1)
	def validateLogin():
		if (True):
			iniciarApp()
		pass
	loginButton = Button(login, text="Login", command=validateLogin).grid(row=2, columnspan=2,sticky=W+E) 
	login.mainloop()

showLogin()
