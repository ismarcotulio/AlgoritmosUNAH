class node:
	def __init__(self,value):
		self.value = value
		self.rightChild = None
		self.leftchild = None

	def get(self):
		
		return self.value

	def set(self, value):
		self.value =value

class BST:
	def __init__(self):
		self.root = None

	def setRoot(self, value):
		self.root = node(value)

	def add(self, value):
		if self.root is None:
			self.setRoot(value)
		else: 
			self.addNode(self.root, value)

	def addNode(self, currentNode, value):
		if currentNode.value >= value:
			if currentNode.leftChild:
				self.addNode(currentNode.leftchild, value)
			else:
				currentNode.leftchild = Node(value)
		elif value > currentNode.value:
			if currentNode.rightChild:
				self.addNode(currentNode.rightChild, value)
			else:
				currentNode.rightChild = Node(value)

	def search(self, value):

	def searchInner(self, currentNode, value):
		if currentNode = None:
			return False

		elif currentNode.value == value:
			return True

		elif currentNode > value:
			return self.searchInner(currentNode.leftChild, value)
		else:
			return self.searchInner(currentNode.rightChild, value)	



