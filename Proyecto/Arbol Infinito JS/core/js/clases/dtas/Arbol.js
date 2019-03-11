import Nodo from "./Nodo.js";

export default class Arbol{

	constructor(){
		console.log("soy un arbol")
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

	/*
	------------------------------------------------------------
	Este seccion que sigue es dedicada a los comandos
	-----------------------------------------------------
	*/	

	comandoControl(comando){
		var lista = comando.split(" ");
		var parametros = [];
		var palabraReservada = null;
		var nombre = null;

		for (var i = 0; i < lista.length; i++) {
			if(i == 0){
				palabraReservada = lista[i];
			}else{
				parametros.push(lista[i]);
			}
		}

		
		try{
			nombre = "comando_"+palabraReservada;
			this["comando_"+palabraReservada](parametros);
			document.getElementById("comando").value = null;
			document.getElementById("terminalMensaje").innerHTML = null;
		}catch(err){
			document.getElementById("terminalMensaje").innerHTML = "Error: comando no existe";
			document.getElementById("comando").value = null;
		}

		
		
	}

	comando_cd(parametros){
		console.log("usted ah seleccionado el comando cd");
	}

	comando_mkdir(parametros){
		console.log("usted ah seleccionado el comando mkdir");
	}

	comando_touch(parametros){
		console.log("usted ah seleccionado el comando touch");
	}

	comando_find(parametros){
		console.log("usted ah seleccionado el comando find");
	}

	comando_pwd(parametros){
		console.log("usted ah seleccionado el comando pwd");
	}

	comando_ls(parametros){
		console.log("usted ah seleccionado el comando ls");
	}

}
