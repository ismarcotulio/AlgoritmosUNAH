class nodo:
	def __init__(self,identificador):
		self.apuntadores = []
		self.identificador = identificador


	def getApuntador(self, valor):
		"""if [valor] in self.apuntadores:
			return self.apuntadores.index(valor)
		else:
			return None"""

		for i in range(len(self.apuntadores)):
			if self.apuntadores[i].identificador == valor:
				return i
			

	def getId(self):
		
		return self.identificador


	def setApuntador(self, valor):
		
		self.apuntadores.append(valor)

	def setId(self, identificador):
		
		self.identificador = identificador


