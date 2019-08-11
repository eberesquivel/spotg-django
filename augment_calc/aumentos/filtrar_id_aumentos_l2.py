import inspect, os

# 178 aumentos existentes
nombre_archivo = "aumentos_id.txt"

palabra_clave_activo = "Trigger"
lista_aumentos_activos = [] #type 1
palabra_clave_chance = "Active"
lista_aumentos_chance = [] #type 2
palabra_clave_pasivo = "Passive"
lista_aumentos_pasivos = [] #type3

def abrirArchivo():
	ruta = os.path.dirname(__file__)
	ruta_completa = ruta + '/' + nombre_archivo
	archivo = open(ruta_completa, 'r')

	return archivo

def leerArchivo(archivo):
	id_anterior = ""
	for linea in archivo.readlines():
		lista_aumento = linea.split("\t")
		id_skill = lista_aumento[0]
		lvl_skill = lista_aumento[1]
		nombre_skill = lista_aumento[2]
		descripcion_skill = lista_aumento[3]

		
		if palabra_clave_activo in descripcion_skill:
			descripcion_skill = descripcion_skill.replace("Trigger", "Active")
			lista_aumento_completo = [id_skill, lvl_skill, nombre_skill, descripcion_skill]
			lista_aumentos_activos.append(lista_aumento_completo)
		elif palabra_clave_chance in descripcion_skill:
			descripcion_skill = descripcion_skill.replace("Active", "Chance")
			lista_aumento_completo = [id_skill, lvl_skill, nombre_skill, descripcion_skill]
			lista_aumentos_chance.append(lista_aumento_completo)
		elif palabra_clave_pasivo in descripcion_skill:
			lista_aumentos_pasivos.append(lista_aumento_completo)
			lista_aumento_completo = [id_skill, lvl_skill, nombre_skill, descripcion_skill]

def crearSQLActivos():
	for skill in lista_aumentos_activos:
		sql = "INSERT INTO augment_skill (id, max_lvl, type, name, description) VALUES (%s,%s,%s,\"%s\",\"%s\");"%(skill[0], skill[1], "1", skill[2], skill[3])
		print(sql)

def crearSQLChances():
	for skill in lista_aumentos_chance:
		sql = "INSERT INTO augment_skill (id, max_lvl, type, name, description) VALUES (%s,%s,%s,\"%s\",\"%s\");"%(skill[0], skill[1], "2", skill[2], skill[3])
		print(sql)

def crearSQLPasivos():
	for skill in lista_aumentos_pasivos:
		sql = "INSERT INTO augment_skill (id, max_lvl, type, name, description) VALUES (%s,%s,%s,\"%s\",\"%s\");"%(skill[0], skill[1], "3", skill[2], skill[3])
		print(sql)

		
archivo_abierto = abrirArchivo()
leerArchivo(archivo_abierto)
crearSQLActivos()
crearSQLChances()
crearSQLPasivos()
