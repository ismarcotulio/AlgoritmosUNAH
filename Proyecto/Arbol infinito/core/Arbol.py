
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
		self.raiz = nodo(identificador,None)


	def agregarNodo(self, nodoActual, identificador):
		if nodoActual.getApuntador(identificador):
			print "error: nodo ya existe"
		elif nodoActual == None:
			nodoActual.setApuntador(nodo(identificador,None))
		else:
			nodoActual.setApuntador(nodo(identificador,nodoActual))

	def nodoActual(self):
		print(" ");
		print self.raiz.identificador
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
			print nodoActual.identificador
			print index
			"""for i in range(len(nodoActual.apuntadores)):
				print nodoActual.apuntadores[i].identificador"""
		 	return self.busquedaInner(nodoActual.apuntadores[index],identificador) 	

	

	def comandoControl(self, comando):

		lista = comando.split()
		Parametros = []

		for i in range(len(lista)):
			if i == 0:
				palabraReservada = lista[i]
			else:
				Parametros.append(lista[i])
				
		nombre = "comando_"+str(palabraReservada)

		ejecucion = getattr(self, nombre)

		ejecucion(Parametros)
		

	def comando_cd(self,parametro):
		print "Has seleccionado el comando cd "+parametro[0]
		if parametro[0] == '...':

			"""codigo"""
		else:
			tipoParametro = parametro[0].split("/")
			if len(tipoParametro)>1:
				print len(tipoParametro)
			elif tipoParametro[0] == "..":
				if self.raiz.padre == None:
					print("Se encuentra en la raiz, no puede retroceder mas")
				else:
					self.raiz = self.raiz.padre
			else:
				index = self.raiz.getApuntador(parametro[0])
				"""print index"""
				if index!=None:
					"""print self.raiz.apuntadores[index].identificador"""
					self.raiz = self.raiz.apuntadores[index]
				else:
					print "directorio no existe"



	def comando_mkdir(self, parametro):
		print "Has seleccionado el comando mkdir "+parametro[0]
		self.agregarNodo(self.raiz, parametro[0])

	def comando_pwd(self):
		print "Has seleccionado el comando pwd"

	def comando_ls(self):
		print "Has seleccionado el comando ls"

	def comando_exit(self):
		print "Has seleccionado el comando exit"