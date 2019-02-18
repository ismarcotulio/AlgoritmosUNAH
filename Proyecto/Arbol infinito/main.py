from core.Arbol import *

estado = 0
arbol = Arbol()
arbol.agregar('raiz')
arbol.agregar('escritorio')
arbol.agregar('ventana')
arbol.agregar('puerta')
arbol.agregar('piso')


while estado == 0:
	arbol.nodoActual()
	comando = raw_input()
	arbol.comandoControl(comando)
	pass


