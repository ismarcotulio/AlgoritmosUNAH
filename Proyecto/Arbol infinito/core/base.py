import json
import os
from nodo import *
from Arbol import *

class base:
	nombre = None
	directorio = None
	datos = {}

	def __init__(self, nombre):
		self.nombre = nombre
		with open(nombre, 'a+') as lectorArchivo:
			"""self.datos = json.loads(lectorArchivo)"""

	

	def insertar(self, instancia):
		with open(self.nombre, 'w') as escritorArchivo:
			json.dump(instancia,escritorArchivo, indent=4, separators=(',', ': '), default=instancia.arbolSerialize)

	def insertarObjeto(self, objeto, padre, identificador):
		existe = False
		for i in range(len(self.datos)):
			if self.datos[i].identificador == identificador:
				if self.datos[i].padre == padre:
					existe = True
				else:
					existe = False
		if existe == False:
			self.datos.append(objeto)	


	def cargar(self):
		with open(self.nombre) as lectorArchivo:
			self.datos = json.load(lectorArchivo)

	"""def eliminarObjeto(self):"""


