from tkinter import messagebox
def consultarLibros(conn):
	conn.db.commit()
	sql_select_query = """SELECT * FROM libro"""
	conn.cursor.execute(sql_select_query)
	return conn.cursor.fetchall()
def consultarLibro(conn, id = -1):
	sql_select_query = """SELECT * FROM libro WHERE id_libro = %s"""
	if id > 0:
		conn.cursor.execute(sql_select_query,id)
		return conn.cursor.fetchall()
	return None
def consultarLibrosObtenidos(conn,id_usuario):
	sql_select_query = """SELECT libro.id_libro,titulo,autor,edicion,publicacion,idioma,editorial,año,saga,paginas,capitulos,sinopsis FROM libro_obtenido, libro WHERE libro_obtenido.id_libro = libro.id_libro and id_usuario = %s"""
	conn.cursor.execute(sql_select_query,id_usuario)
	return conn.cursor.fetchall()
def consultarLibrosDeseados(conn, id_usuario):
	sql_select_query = """SELECT libro.id_libro,titulo,autor,edicion,publicacion,idioma,editorial,año,saga,paginas,capitulos,sinopsis FROM libro_deseado, libro WHERE libro_deseado.id_libro = libro.id_libro and id_usuario = %s"""
	conn.cursor.execute(sql_select_query,id_usuario)
	return conn.cursor.fetchall()	
def consultarLibrosLeidos(conn, id_usuario):
	sql_select_query = """SELECT libro.id_libro,titulo,autor,edicion,publicacion,idioma,editorial,año,saga,paginas,capitulos,sinopsis FROM libro_leido, libro WHERE libro_leido.id_libro = libro.id_libro and id_usuario = %s"""
	conn.cursor.execute(sql_select_query,id_usuario)
	return conn.cursor.fetchall()
def cantidadLibrosObtenidos(conn, id_usuario):
	return len(consultarLibrosObtenidos(conn,id_usuario))
def cantidadLibrosDeseados(conn, id_usuario):
	return len(consultarLibrosDeseados(conn,id_usuario))
def cantidadLibrosLeidos(conn, id_usuario):
	return len(consultarLibrosLeidos(conn,id_usuario))

def agregarLibroColeccion(conn,id_usuario,id_libro,fecha):
	sql_insert_query = """INSERT INTO libro_obtenido VALUES(Null,%s,%s,%s)"""
	sql_select_query = """SELECT * FROM libro_obtenido WHERE id_libro = %s and id_usuario = %s"""
	conn.cursor.execute(sql_select_query,(id_libro, id_usuario))
	if len(conn.cursor.fetchall())<1:
		try:
			conn.cursor.execute(sql_insert_query,(id_usuario,id_libro,fecha))
			conn.db.commit()
			return True
		except:
			messagebox.showerror("Error Coleccion", "Error al agregar ese libro a la coleccion")
			do.rollback()
			return False
	else:
		messagebox.showerror("Error Coleccion", "Error ese libro ya esta en tu coleccion")

def eliminarLibroDeseado(conn,id_usuario,id_libro):
	print("Borrando")
	sql_delete_query = """DELETE FROM libro_deseado WHERE id_usuario = %s and id_libro = %s """
	try:
		conn.cursor.execute(sql_delete_query,(id_usuario,id_libro))
		conn.db.commit()
		print("Borrado")
		return True
	except:
		messagebox.showerror("Error Deseados", "Error al eliminar ese libro a los deseados")
		do.rollback()
		return False