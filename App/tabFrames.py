from tkinter import *
from tkinter import ttk
from tkinter.font import *
def crearTabla(tab,rows,nombre):
	titulo = Label(tab, text=nombre, font=("Helvetica", 16))
	headers = ['Titulo','Autor',"Idioma","Año","Saga"]
	tree = ttk.Treeview(tab, columns=headers, show="headings")
	
	titulo.pack(side=TOP, fill="x")
	vsb = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
	vsb.pack(side='right', fill='y')
	hsb = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
	hsb.pack(side='bottom', fill='x')
	tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
	def treeViewListener(event):
		print(tree.item(tree.selection(),'text'))
	tree.bind('<<TreeviewSelect>>',treeViewListener)
	for header in headers:
		tree.heading(header, text=header.title())
	for i in range(len(rows)):
		tree.insert('', 'end',text=rows[i][0], values=(rows[i][1],rows[i][2],rows[i][5],rows[i][7],rows[i][8]))
	tree.pack(expand=1, fill='both')
	return tree
def actualizarTabla(tree,rows):
	tree.delete(*tree.get_children())
	for i in range(len(rows)):
		tree.insert('', 'end',text=rows[i][0], values=(rows[i][1],rows[i][2],rows[i][5],rows[i][7],rows[i][8]))
def tabGaleria(tab,rows,tree):
	tab = ttk.Frame(notebook)
	titulo = Label(tab, text="Galeria", font=("Helvetica", 16))
	headers = ['Titulo','Autor',"Idioma","Año","Saga"]
	tree = ttk.Treeview(tab, columns=headers, show="headings")
	
	titulo.pack(side=TOP, fill="x")
	vsb = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
	vsb.pack(side='right', fill='y')
	hsb = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
	hsb.pack(side='bottom', fill='x')
	tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
	def treeViewListener(event):
		print(tree.item(tree.selection(),'text'))
	tree.bind('<<TreeviewSelect>>',treeViewListener)
	for header in headers:
		tree.heading(header, text=header.title())
		
			
	for i in range(len(rows)):
		for j in range(len(headers)):
			tree.column(headers[j], width=int(620/5))
		tree.insert('', 'end',text=rows[i][0], values=(rows[i][1],rows[i][2],rows[i][5],rows[i][7],rows[i][8]))
	tree.pack(expand=1, fill='both')
	return tab
def tabLibro(notebook,rows):
	tab = ttk.Frame(notebook)
	titulo = Label(tab, text="Galeria", font=("Helvetica", 16))
	headers = ['Titulo','Autor',"Idioma","Año","Saga"]
	tree = ttk.Treeview(tab, columns=headers, show="headings")
	
	titulo.pack(side=TOP, fill="x")
	vsb = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
	vsb.pack(side='right', fill='y')
	hsb = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
	hsb.pack(side='bottom', fill='x')
	tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
	def treeViewListener(event):
		print(tree.item(tree.selection(),'text'))
	tree.bind('<<TreeviewSelect>>',treeViewListener)
	for header in headers:
		tree.heading(header, text=header.title())
		
			
	for i in range(len(rows)):
		for j in range(len(headers)):
			tree.column(headers[j], width=int(620/5))
		tree.insert('', 'end',text=rows[i][0], values=(rows[i][1],rows[i][2],rows[i][5],rows[i][7],rows[i][8]))
	tree.pack(expand=1, fill='both')
	return tab

	