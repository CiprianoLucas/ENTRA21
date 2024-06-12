//Será alert mostrado?

if ("0") {
    alert( 'Hello' );
  }
  // Sim

//Usando a if..elseconstrução, escreva o código que pergunta: 'Qual é o nome “oficial” do JavaScript?'
//Se o visitante inserir “ECMAScript”, então imprima “Certo!”, caso contrário – imprima: “Você não sabe? ECMAScript!”

let nameJavascript = prompt("Qual o nome oficial do Javascript?");

if(nameJavascript === "ECMAScript"){
    alert("Correto");
}
else{
    alert("Errado");
}

//Usando if..else, escreva o código que obtém um número prompte depois mostra alert:
//1, se o valor for maior que zero,
//-1, se for menor que zero,
//0, se for igual a zero.
//Nesta tarefa assumimos que a entrada é sempre um número.

let number = +prompt("Escolha um número");

if(number > 0){
    alert(1);
}
else if(number === 0){
    alert(0);
}
else {
    alert(-1);
}

//Reescreva isso ifusando o operador condicional '?':

/*
let result;

if (a + b < 4) {
  result = 'Below';
} else {
  result = 'Over';
}
*/
let result;
let a = 1;
let b = 7;
result = (a + b < 4) ? "Below" : "Over";
alert(result);

//Reescreva if..elseusando vários operadores ternários '?'.
//Para facilitar a leitura, é recomendado dividir o código em várias linhas.

let message;
message = (login == 'Employee') ? 'Hello' : (login == 'Director') ? 'Greetings' : (login == '') ? 'No login' : '';