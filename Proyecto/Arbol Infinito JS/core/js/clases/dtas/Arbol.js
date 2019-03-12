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
		var nodo = nodoActual.getHijo(identificador);
		if(nodo != null){
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
			document.getElementById("terminalError").innerHTML = null;
		}catch(err){
			document.getElementById("terminalError").innerHTML = err.message;
			document.getElementById("comando").value = null;
		}

		
		
	}

	comando_cd(parametro){
		console.log("usted ah seleccionado el comando cd");
		var tipoParametro = parametro[0].split("/");
		if(tipoParametro.length > 1){
			console.log("ruta relativa");
		}else{
			if(tipoParametro[0] == ".."){
				console.log("ruta retroceso");
				if(this.raiz.padre == null){
					document.getElementById("terminalMensaje").innerHTML = "Error: Se encuentra en la ruta raiz, no puede retroceder mas";
				}else{
					this.raiz = this.raiz.padre;
					document.getElementById("terminalMensaje").innerHTML = "Ahora se encuentra en el directorio "+this.raiz.identificador;
				}
			}else{
				console.log("ruta absoluta");
				var objeto = this.raiz.getHijo(parametro[0]);

				if(objeto != null){
					this.raiz = objeto;
					document.getElementById("terminalMensaje").innerHTML = "Ahora se encuentra en el directorio "+this.raiz.identificador;
				}else{
					document.getElementById("terminalMensaje").innerHTML = "Error: Directorio no existe";
				}

			}
		}
	}

	comando_mkdir(parametro){
		console.log("usted ah seleccionado el comando mkdir");
		this.agregarNodo(this.raiz, parametro[0]);
		document.getElementById("terminalMensaje").innerHTML = "Se creo el directorio "+parametro[0];
	}

	comando_touch(parametro){
		console.log("usted ah seleccionado el comando touch");
	}

	comando_find(parametro){
		console.log("usted ah seleccionado el comando find");
	}

	comando_pwd(parametro){
		console.log("usted ah seleccionado el comando pwd");
	}

	comando_ls(parametro){
		console.log("usted ah seleccionado el comando ls");
	}

}
