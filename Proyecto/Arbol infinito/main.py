from core.Arbol import *

estado = 0
arbol = Arbol()

#arbol.base.cargar()
#arbol.base.insertarArbol(arbol.base.datos)
print(" ")
arbol.agregar('raiz')
print(arbol.dic)



while estado == 0:
	arbol.nodoActual()
	comando = raw_input()
	if comando == "exit":
		arbol.toRaiz()
		arbol.base.insertar(arbol)
		print("Ha seleccionado el comando exit")
		print("Gracias por utilizar la terminal")
		print(" ")
		estado = 1
	else:
		arbol.comandoControl(comando)
	
	pass


