from tkinter import messagebox
def validarDatosRegistro(nombre, primerapellido, segundoapellido, usuario, password, repassword):
	if (any(x.isalpha() for x in nombre) and all(x.isalpha() or x.isspace() for x in nombre)):
		if (any(x.isalpha() for x in primerapellido) and all(x.isalpha() or x.isspace() for x in primerapellido)):
			if (any(x.isalpha() for x in segundoapellido) and all(x.isalpha() or x.isspace() for x in segundoapellido)):
				if (any(x.isalpha() for x in usuario) and all(x.isalpha() for x in usuario)):
					if (len(password)>3):
						if password == repassword:
							return True
						else:
							messagebox.showerror("Contraseña Invalida", "Las Contraseñas no coinciden")	
					else:
						messagebox.showerror("Contraseña Invalida", "La Contraseña debe tener al menos 4 caracteres")	
				else:
					messagebox.showerror("Usuario Invalido", "El Usuario debe contener solo letras")	
			else:
				messagebox.showerror("Segundo Apellido Invalido", "El Apellido debe contener solo letras y espacios")
		else:
			messagebox.showerror("Primer Apellido Invalido", "El Apellido debe contener solo letras y espacios")
	else:
		messagebox.showerror("Nombre Invalido", "El Nombre debe contener solo letras y espacios")
	return False
def validarDatosInicioSesion(usuario, password):
	if (any(x.isalpha() for x in usuario) and all(x.isalpha() for x in usuario)):
		if (len(password)>3):
			return True
		else:
			messagebox.showerror("Contraseña Invalida", "La Contraseña debe tener al menos 4 caracteres")	
	else:
		messagebox.showerror("Usuario Invalido", "El Usuario debe contener solo letras")
	return False