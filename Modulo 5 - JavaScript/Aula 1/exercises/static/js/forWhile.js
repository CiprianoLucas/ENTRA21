//Qual é o último valor alertado por este código? Por que?

let i = 3;

while (i) {
  alert( i-- );
}

// O último valor será 1, pois 0 é considerado como False


//Para cada iteração do loop, anote o valor gerado e compare-o com a solução.
//Ambos os loops alert têm os mesmos valores ou não?

let j = 0;
while (++j < 5) alert( j );// 1,2,3,4

let k = 0;
while (k++ < 5) alert( k );//1,2,3,4,5



//Produza números pares no loop

for (let i=0; i<=10; i += 2){
    alert(i)
}

//Substitua for por while

/*for (let i = 0; i < 3; i++) {
    alert( `number ${i}!` );
  }
*/

let l = 0
while(l < 3){
    alert(l)
    l++
}