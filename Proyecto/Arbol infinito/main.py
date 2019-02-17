from core.Arbol import *

estado = 0
arbol = Arbol()
arbol.agregar('raiz')

while estado == 0:
	comando = raw_input()
	arbol.comandoControl(comando)
	pass
"""
arbol.agregar('escritorio')
arbol.agregar('ventana')
arbol.agregar('puerta')
arbol.agregar('piso')

arbol.busqueda('piso')
"""