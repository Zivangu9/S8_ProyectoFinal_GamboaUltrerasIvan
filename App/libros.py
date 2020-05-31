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
def cantidadLibrosLeidos(conn, id_usuario):
	sql_select_query = """SELECT * FROM libro_leido WHERE id_usuario = %s"""
	conn.cursor.execute(sql_select_query,id_usuario)
	return len(conn.cursor.fetchall())
def cantidadLibrosObtenidos(conn, id_usuario):
	sql_select_query = """SELECT * FROM libro_obtenido WHERE id_usuario = %s"""
	conn.cursor.execute(sql_select_query,id_usuario)
	return len(conn.cursor.fetchall())
def cantidadLibrosDeseados(conn, id_usuario):
	sql_select_query = """SELECT * FROM libro_deseado WHERE id_usuario = %s"""
	conn.cursor.execute(sql_select_query,id_usuario)
	return len(conn.cursor.fetchall())
	