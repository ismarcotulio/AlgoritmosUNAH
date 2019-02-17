
from nodo import *
from comandos.cd import *
from comandos.mkdir import *
from comandos.pwd import *
from comandos.ls import *
from comandos.touch import *
from comandos.mv import *
from comandos.rm import *
from comandos.exit import *
from comandos.find import *


class Arbol:
	def __init__(self):

		self.raiz = None

	def agregar(self, identificador):
		if self.raiz is None:
			self.setRaiz(identificador)
		else: 
			self.agregarNodo(self.raiz, identificador)

	def setRaiz(self, identificador):
		self.raiz = nodo(identificador)


	def agregarNodo(self, nodoActual, identificador):
		if nodoActual.getApuntador(identificador):
			print "error: nodo ya existe"
		else:
			nodoActual.setApuntador(nodo(identificador))


		"""if nodoActual.valor >= valor:
			if nodoActual.hijoIzquierdo:
				self.agregarNodo(nodoActual.hijoDerecho, valor)
			else:
				nodoActual.hijoDerecho = Nodo(valor)
		elif valor > nodoActual.valor:
			if nodoActual.hijoIzquierdo:
				self.agregarNodo(nodoActual.hijoIzquierdo, valor)
			else:
				nodoActual.hijoIzquierdo = Nodo(valor)"""


	def busqueda(self,identificador):
		self.busquedaInner(self.raiz,identificador)

	def busquedaInner(self, nodoActual, identificador):
		if nodoActual == None:
			return False

		elif nodoActual.identificador == identificador:
			return True

		else:
			index = nodoActual.getApuntador(identificador)
			print index 
			print nodoActual.identificador
			for i in range(len(nodoActual.apuntadores)):
				print nodoActual.apuntadores[i].identificador
		 	return self.busquedaInner(nodoActual.apuntadores[index],identificador) 	

	

	def comandoControl(self, comando):
		
		nombre = "comando_"+str(comando)

		ejecucion = getattr(self, nombre, lambda: "comando invalido")

		return ejecucion()
		

	def comando_cd(self):
		print "Has seleccionado el comando cd"

	def comando_mkdir(self):
		print "Has seleccionado el comando mkdir"

	def comando_pwd(self):
		print "Has seleccionado el comando pwd"

	def comando_ls(self):
		print "Has seleccionado el comando ls"

	def comando_exit(self):
		print "Has seleccionado el comando exit"