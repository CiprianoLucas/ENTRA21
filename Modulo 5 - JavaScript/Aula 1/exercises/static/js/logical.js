//Qual será a saída do código abaixo?
alert( null || 2 || undefined ); //2
alert( alert(1) || 2 || alert(3) ); //1 depois 2
alert( 1 && null && 2 );//Null
alert( alert(1) && alert(2) );//1 depois undefined
alert( null || 2 && 3 || 4 );//3

//Escreva uma ifcondição para verificar se ageestá entre 14e 90inclusivamente.
//“Inclusivamente” significa que agepode atingir as bordas 14ou 90.

let age = 13;

(age >= 14 && age <= 90) ? alert("Está no range") : alert("Não está no range");

//Qual destes alerts vai ser executado?
//Quais serão os resultados das expressões dentro if(...)?

if (-1 || 0) alert( 'first' );//Sim
if (-1 && 0) alert( 'second' );//Não
if (null || -1 && 1) alert( 'third' );// Sim
