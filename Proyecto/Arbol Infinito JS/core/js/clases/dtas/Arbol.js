import Nodo from "./Nodo.js";

export default class Arbol{

	constructor(){
		alert("soy un arbol")
		this.raiz = null;
	}

	agregar(identificador){
		if(this.raiz == null){
			this.agregarRaiz(identificador);
		}else{
			this.agregarNodo(this.raiz, identificador);
		}
	}

	agregarRaiz(identificador){
		this.raiz = new Nodo(identificador,null);
	}

	agregarNodo(nodoActual, identificador){
		if(nodoActual.getHijo(identificador) != null){
			alert("error el nodo ya existe");
		}else{
			nodoActual.setHijo(new Nodo(identificador,nodoActual));
		}
	}	

}
