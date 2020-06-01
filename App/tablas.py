from tkinter import *
from tkinter import ttk
from tkinter.font import *
def crearTabla(tab,rows,nombre):
	titulo = Label(tab, text=nombre, font=("Bookman Old Style", 18))
	headers = ['Titulo','Autor','Edicion','Publicacion','Idioma','Editorial','Año','Saga','Paginas','Capitulos']
	tree = ttk.Treeview(tab, columns=headers, show="headings")
	titulo.pack(side=TOP, fill="x")
	vsb = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
	vsb.pack(side='right', fill='y')
	hsb = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
	hsb.pack(side='bottom', fill='x')
	tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
	tree.column(headers[0], width=300)
	tree.column(headers[1], width=100)
	tree.column(headers[2], width=50)
	tree.column(headers[3], width=150)
	tree.column(headers[4], width=80)
	tree.column(headers[5], width=150)
	tree.column(headers[6], width=40)
	tree.column(headers[7], width=120)
	tree.column(headers[8], width=50)
	tree.column(headers[9], width=80)
	for header in headers:
		tree.heading(header, text=header.title())

	actualizarTabla(tree,rows)
	tree.pack(expand=1, fill='both')
	return tree
def crearTablaLista(tab,rows,nombre):
	titulo = Label(tab, text=nombre, font=("Bookman Old Style", 18))
	headers = ['Fecha','Titulo','Autor','Edicion','Publicacion','Idioma','Editorial','Año','Saga','Paginas','Capitulos']
	tree = ttk.Treeview(tab, columns=headers, show="headings")
	titulo.pack(side=TOP, fill="x")
	vsb = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
	vsb.pack(side='right', fill='y')
	hsb = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
	hsb.pack(side='bottom', fill='x')
	tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
	tree.column(headers[0], width=80)
	tree.column(headers[1], width=300)
	tree.column(headers[2], width=100)
	tree.column(headers[3], width=50)
	tree.column(headers[4], width=150)
	tree.column(headers[5], width=80)
	tree.column(headers[6], width=150)
	tree.column(headers[7], width=40)
	tree.column(headers[8], width=120)
	tree.column(headers[9], width=50)
	tree.column(headers[10], width=80)
	for header in headers:
		tree.heading(header, text=header.title())
	actualizarTablaLista(tree,rows)
	tree.pack(expand=1, fill='both')
	return tree
def isNone(value):
	if value == None:
		return ''
	return value
def actualizarTabla(tree,rows):
	tree.delete(*tree.get_children())
	for i in range(len(rows)):
		tree.insert('', 'end',text=rows[i][0], values=(isNone(rows[i][1]),isNone(rows[i][2]),isNone(rows[i][3]),isNone(rows[i][4]),isNone(rows[i][5]),isNone(rows[i][6]),isNone(rows[i][7]),isNone(rows[i][8]),isNone(rows[i][9]),isNone(rows[i][10])))
def actualizarTablaLista(tree,rows):
	tree.delete(*tree.get_children())
	for i in range(len(rows)):
		tree.insert('', 'end',text=rows[i][0], values=(isNone(rows[i][1]),isNone(rows[i][2]),isNone(rows[i][3]),isNone(rows[i][4]),isNone(rows[i][5]),isNone(rows[i][6]),isNone(rows[i][7]),isNone(rows[i][8]),isNone(rows[i][9]),isNone(rows[i][10]),isNone(rows[i][11])))