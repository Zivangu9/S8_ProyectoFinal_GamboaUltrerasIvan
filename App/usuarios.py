def registrarUsuario(conn, nombre, primerApe, segundoApe, username, password):
	sql_insert_query = """INSERT INTO usuario(nombre,primer_apellido,segundo_apellido,usuario,clave) VALUES(%s,%s,%s,%s,SHA1(%s))"""
	try:
		conn.cursor.execute(sql_insert_query,(nombre,primerApe,segundoApe,username,password))
		conn.db.commit()
		return True
	except:
		messagebox.showerror("Error Usuario", "Ese Usuario ya existe")
		do.rollback()
		return False
def iniciarSesion(conn, usuario, clave):
	sql_select_query = """SELECT id_usuario FROM usuario WHERE usuario = %s AND clave = SHA1(%s)"""
	conn.cursor.execute(sql_select_query,(usuario,clave))
	rows = conn.cursor.fetchall()		
	if (len(rows)==1):
		return int(rows[0][0])
	return None
def consultarNombre(conn, id_usuario):
	if id_usuario is None:
		return ''
	sql_select_query = """SELECT nombre, primer_apellido, segundo_apellido FROM usuario WHERE id_usuario = %s"""
	conn.cursor.execute(sql_select_query,(id_usuario))
	rows = conn.cursor.fetchall()		
	if (len(rows)==1):
		return rows[0][0]+rows[0][1]+rows[0][2]
	return ""