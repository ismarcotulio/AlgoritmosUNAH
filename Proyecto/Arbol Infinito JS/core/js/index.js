import Arbol from "./clases/dtas/Arbol.js";

var arbol = new Arbol();
arbol.agregar("raiz");

var startButton = document.getElementById("start");
var terminal = document.getElementById("terminal");
var	enviarComando = document.getElementById("enviarComando");
var Inputcomando = document.getElementById("comando"); 



startButton.addEventListener("click", function(){
	startButton.style.display = "none";
	terminal.style.display = "block";
});

enviarComando.addEventListener("click", function(){
	
	comando = Inputcomando.value;
	console.log(comando);

	if(comando == "exit"){
		startButton.style.display = "block";
		terminal.style.display = "none";
		Inputcomando.value = null;
	}else{
		arbol.comandoControl(comando);
	}
});


