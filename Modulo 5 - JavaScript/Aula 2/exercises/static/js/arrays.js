/*
Vamos tentar 5 operações de array.

Crie um array stylescom os itens “Jazz” e “Blues”.
Adicione “Rock-n-Roll” ao final.
Substitua o valor do meio por “Clássicos”. Seu código para encontrar o valor médio deve funcionar para qualquer array com comprimento ímpar.
Retire o primeiro valor do array e mostre-o.
Anexe Rape Reggaeao array.
*/

const styles = ["Jazz", "Blues"];
styles.push("Rock-n-Roll");
styles[Math.floor(styles.length/2)] = "Clássicos"
styles.pop(-1)
styles.push("Rape", "Reggae")
console.log(styles)

//Somar os números de entrada
let number = prompt("Um número")
const numbers = []
while (!isNaN(number) && number!= null){
    numbers.push(number)
    console.log(numbers)
    number = prompt("Um número")
}

const sumInput = (numbers) => {
    let acumulator = 0
    for(let i of numbers){
        acumulator += Number(i)
    }
    return acumulator
}

console.log(sumInput(numbers))