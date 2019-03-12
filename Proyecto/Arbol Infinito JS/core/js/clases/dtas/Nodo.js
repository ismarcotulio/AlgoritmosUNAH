export default class Nodo{

	constructor(identificador,padre){
		console.log("Soy un nodo");
		this.identificador = identificador;
		this.padre = padre;
		this.apuntadores = [];
	}

	getHijo(identificador){
		var respuesta = null;
		this.apuntadores.forEach(function(item){
			if(item.identificador == identificador){
				console.log("se encontro");
				console.log(item);
				respuesta = item;
			}
		});
		return respuesta;

	}

	setHijo(nodo){
		this.apuntadores.push(nodo);
	}
}