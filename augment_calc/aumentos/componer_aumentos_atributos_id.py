import inspect, os

# 178 aumentos existentes
nombre_archivo = "aumentos_atributos_id.txt"

lista_atributos_aumento = []
def abrirArchivo():
	ruta = os.path.dirname(__file__)
	ruta_completa = ruta + '/' + nombre_archivo
	archivo = open(ruta_completa, 'r')

	return archivo

def leerArchivo(archivo):
	for linea in archivo.readlines():
		linea_limpia = linea.replace("\n", "")
		attribute_id = linea_limpia[:5]
		attribute_description = linea_limpia[6:]

		if "Active" in attribute_description:
			lista_atributos_aumento.append([attribute_id, attribute_description, "1"])
		elif "Chance" in attribute_description:
			lista_atributos_aumento.append([attribute_id, attribute_description, "2"])
		elif "Passive" in attribute_description:
			lista_atributos_aumento.append([attribute_id, attribute_description, "3"])


def imprimirAtributos():
	for aumento in lista_atributos_aumento:
		print("\t".join(aumento))
archivo_abierto = abrirArchivo()
leerArchivo(archivo_abierto)
imprimirAtributos()