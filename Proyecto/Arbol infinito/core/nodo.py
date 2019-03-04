class nodo:
	identificador = None
	padre = None
	apuntadores = []


	def __init__(self,identificador,padre):
		self.apuntadores = []
		self.identificador = identificador
		self.padre = padre


	@staticmethod
    	def serialize(obj):
    		hijo={}
    		print("---------------------------obj------------------------------------")
    		print(obj)
    		print(type(obj))
    		print(obj.identificador)
    		if(len(obj.apuntadores) != 0):
    			print("------------------------------hijos-------------------------------")
    			print(obj.apuntadores)
    			print(type(obj.apuntadores))
    			for item in obj.apuntadores:
    				print("------------------item-------------------------------------------")
    				print(item)
    				print(type(item))
    				print(item.identificador)
    				hijo = obj.serialize(item)
    		
    		

		return {
		   "dic "+item.identificador:
			item.identificador,
						"hijos "+item.identificador:[
						Arbol.serialize(item)
						]	
		}




	def getApuntador(self, valor):
		"""if [valor] in self.apuntadores:
			return self.apuntadores.index(valor)
		else:
			return None"""

		for item in self.apuntadores:
			if item.identificador == valor:
				return item


	def getId(self):
		
		return self.identificador


	def setApuntador(self, valor):
		
		self.apuntadores.append(valor)

	def setId(self, identificador):
		
		self.identificador = identificador


