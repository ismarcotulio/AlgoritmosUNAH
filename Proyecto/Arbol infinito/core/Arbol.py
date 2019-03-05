
from nodo import *
from base import *
import json



class Arbol:
	raiz = None
	nivel = 0
	base = base('base.json') 
	hijos = {}		
	dic = {}
	find = None

	def __init__(self):
		pass

	def agregar(self, identificador):
		if self.raiz is None:
			self.setRaiz(identificador)
		else: 
			self.agregarNodo(self.raiz, identificador)

	def setRaiz(self, identificador):
		self.raiz = nodo(identificador,None)
		#self.raizPadre = nodo(identificador,None)
		"""self.base.insertarObjeto(self.raiz,self.raiz.padre, self.raiz.identificador)"""
		


	def agregarNodo(self, nodoActual, identificador):
		if nodoActual.getApuntador(identificador) != None:
			print("error: nodo ya existe")
		else:
			nodoActual.setApuntador(nodo(str(identificador),nodoActual))
			#self.base.insertarObjeto(nodo(identificador,nodoActual),nodoActual.identificador,identificador)

	def nodoActual(self):
		print(" ");
		print(self.raiz.identificador)
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


	"""def busqueda(self,identificador):
		self.busquedaInner(self.raiz,identificador)

	def busquedaInner(self, nodoActual, identificador):
		if nodoActual == None:
			return False

		elif nodoActual.identificador == identificador:
			return True

		else:
			index = nodoActual.getApuntador(identificador)
			print(nodoActual.identificador)
			print(index)
			for i in range(len(nodoActual.apuntadores)):
				print nodoActual.apuntadores[i].identificador
		 	return self.busquedaInner(nodoActual.apuntadores[index],identificador)""" 	
	

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
		print("Has seleccionado el comando cd "+parametro[0])
		if parametro[0] == '...':

			"""codigo"""
		else:
			tipoParametro = parametro[0].split("/")
			if len(tipoParametro)>1:
				print(len(tipoParametro))
			elif tipoParametro[0] == "..":
				if self.raiz.padre == None:
					print("Se encuentra en la raiz, no puede retroceder mas")
				else:
					self.raiz = self.raiz.padre
					self.nivel = self.nivel - 1
			else:
				
				obj = self.raiz.getApuntador(parametro[0])
				"""print index"""
				if obj != None:
					"""print self.raiz.apuntadores[index].identificador"""
					self.raiz = obj
					self.nivel = self.nivel + 1
				else:
					print("directorio no existe")

	def toRaiz(self):
		while self.raiz.identificador != "raiz":
			self.raiz = self.raiz.padre
			#self.nivel = self.nivel - 1

	def comando_mkdir(self, parametro):
		print("Has seleccionado el comando mkdir "+parametro[0])
		self.agregarNodo(self.raiz, parametro[0])

	def comando_pwd(self, parametro):
		print("Has seleccionado el comando pwd")
		print("Usted se encuentra en el nodo: ")
		self.nodoActual()

	def comando_ls(self):
		print("Has seleccionado el comando ls")

	def comando_exit(self, base):
		print("Has seleccionado el comando exit")


	def comando_find(self, parametro):
		
		if(len(parametro) == 1):
			print("Has seleccionado el comando find "+parametro[0])
			self.toRaiz()	
			Arbol.buscar(self.raiz, parametro[0])
			if(Arbol.find != None):
				self.raiz = Arbol.find		
			else:
				print("directorio no encontrado")
		else:
			print("ha introducido muchos parametros, intentelo de nuevo")


	@staticmethod
	def serialize(obj):
		"""print("---------------------------obj------------------------------------")
		print(obj)
		print(type(obj))
		print(obj.identificador)"""
		if(len(obj.apuntadores) != 0):
			"""print("------------------------------hijos-------------------------------")
			print(obj.apuntadores)
			print(type(obj.apuntadores))"""
			for item in obj.apuntadores:
				"""print("------------------item-------------------------------------------")
				print(item)
				print(type(item))
				print(item.identificador)"""
				Arbol.dic = {
					"dic "+item.identificador:
						item.identificador,
						"hijos "+item.identificador:[
							Arbol.serialize(item)
						]	
					}
		return Arbol.dic
    				
	@staticmethod
	def arbolSerialize(obj):
		obj.hijos = {
			"dic "+obj.raiz.identificador:
				obj.raiz.identificador,
				"hijos "+obj.raiz.identificador:[
					obj.serialize(obj.raiz)
				]
		}

		
		return obj.hijos

	"""def raizSerialize(self, obj):
		raiz = self.raiz
		self.hijos.setdefault("raiz", raiz)
		print(self.hijos)
		print(" ")
		
		return self.hijos
"""

	@staticmethod
	def buscar(obj, identificador):
		if obj.identificador == identificador:
			print("encontrado")
			return obj
		else:
			if len(obj.apuntadores) > 0:
				for item in obj.apuntadores:
					
					if(item.identificador == str(identificador)):
						print("encontrado")
						Arbol.find = item
					else:
						Arbol.buscar(item, identificador)
