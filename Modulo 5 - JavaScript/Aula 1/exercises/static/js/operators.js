//Quais são os valores finais de todas as variáveis a, be após o código abaixo c d

/*
let a = 1, b = 1;

let c = ++a; // 2
let d = b++; // 1
*/

// a = 2
// b = 2
// c = 2
// d = 1

//What are the values of y and x after the code below?

let y = 2;

let x = 1 + (y *= 2);

// x = 5
// y = 4

//What are results of these expressions?

"" + 1 + 0; // string 10
"" - 1 + 0; // number -1
true + false; // number 1
6 / "3"; // number 2
"2" * "3"; // number 6
4 + 5 + "px"; // string 9px
"$" + 4 + 5; // string $45
"4" - 2; // number 2
"4px" - 2; // NaN
"  -9  " + 5; // string    -9   5
"  -9  " - 5; // number -14
null + 1; // number 1
undefined + 1; // NaN
" \t \n" - 2; // number -2

//Aqui está um código que pede dois números ao usuário e mostra sua soma.
//Funciona incorretamente. A saída no exemplo abaixo é 12(para valores de prompt padrão).
//Por que? Consertá-lo. O resultado deveria ser 3.

let a = prompt("First number?", 1);
let b = prompt("Second number?", 2);

//alert((a) + b);
alert(Number(a) + Number(b));

console.log(" \t \n" - 2);