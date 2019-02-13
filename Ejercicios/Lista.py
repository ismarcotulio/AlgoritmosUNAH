class Lista:
	def __init__(self,contents=[], size=10):
		 
		self = [None] * size
		#self.numItems = 0
		#self.size = size
		
		for e in contents:
			self.append(e)

	def __getitem__(self,index):
		if index >= 0 and index < self.numItems:
			return self.items[index]

		raise IndexError("PyList index out of range")

	def __setitem__(self,index,val):
		if index >= 0 and index < self.numItems:
			self.items[index] = val
			return

		raise IndexError("PyList assignment index out of range")

	def __add__(self,other):
		result = PyList(size=self.numItems+other.numItems)

		for i in range(self.numItems):
			result.append(self.items[i])

		for i in range(other.numItems):
			result.append(other.items[i])

		return result


	def __makeroom(self):

		newlen = (self.size // 4) + self.size + 1
		newlst = [None] * newlen
		for i in range(self.numItems):
			newlst[i] = self.items[i]

		self.items = newlst
		self.size = newlen

	def append(self,item):
		if self.numItems == self.size:
			self.__makeroom()

		self.items[self.numItems] = item
		self.numItems += 1

sampleList = Lista(["a", "b", "c"])



