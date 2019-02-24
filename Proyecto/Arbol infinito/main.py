from core.Arbol import *

estado = 0
arbol = Arbol()
arbol.agregar('raiz')



while estado == 0:
	arbol.nodoActual()
	comando = raw_input()
	arbol.comandoControl(comando)
	pass


