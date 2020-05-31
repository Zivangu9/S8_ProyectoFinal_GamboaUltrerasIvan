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