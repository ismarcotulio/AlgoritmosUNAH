export default class Nodo{

	constructor(identificador,padre){
		console.log("Soy un nodo");
		this.identificador = identificador;
		this.padre = padre;
		this.apuntadores = [];
	}

	getHijo(identificador){
		this.apuntadores.forEach(function(item){
			if(item.identificador == identificador){
				return item;
			}
		});
	}

	setHijo(nodo){
		this.apuntadores.push(nodo);
	}
}