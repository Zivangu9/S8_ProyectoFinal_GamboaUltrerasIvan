def consultarLibros(conn):
	conn.db.commit()
	sql_select_query = """SELECT * FROM libro"""
	conn.cursor.execute(sql_select_query)
	return conn.cursor.fetchall()
def consultarLibro(conn, id = -1):
	sql_select_query = """SELECT * FROM libro WHERE id_libro = %i"""
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
	sql_select_query = """SELECT * FROM libro_leido WHERE id_usuario = %s"""
	conn.cursor.execute(sql_select_query,id_usuario)
	return conn.cursor.fetchall()
def cantidadLibrosObtenidos(conn, id_usuario):
	return len(consultarLibrosObtenidos(conn,id_usuario))
def cantidadLibrosDeseados(conn, id_usuario):
	return len(consultarLibrosDeseados(conn,id_usuario))
def cantidadLibrosLeidos(conn, id_usuario):
	return len(consultarLibrosLeidos(conn,id_usuario))

