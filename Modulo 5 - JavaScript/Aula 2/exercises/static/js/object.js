/*
Escreva o código, uma linha para cada ação:

Crie um objeto vazio user.
Adicione a propriedade namecom o valor John.
Adicione a propriedade surnamecom o valor Smith.
Altere o valor de namepara Pete.
Remova a propriedade namedo objeto.
*/

let user = {};
user.name = "John";
user.surname = "Smith";
user.name = "Pete";
delete user.name;

console.log(user.surname)


//Crie uma função multiplyNumeric(obj)que multiplique todos os valores de propriedades numéricas de objpor 2.

let menu = {
    width: 200,
    height: 300,
    title: "My menu"
  };

const multiplyNumeric = (obj) => {
 for (let key in obj){

    if (typeof obj[key] == "number"){
        obj[key] *= 2;
    }
 }
}

multiplyNumeric(menu);

console.log(menu.width);
console.log(menu.height);
console.log(menu.title);

//Escreva o código para somar todos os salários e armazenar na variável sum. Deveria estar 390no exemplo acima.

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
  }

acumulator = 0
for (let key in salaries){
    acumulator += salaries[key];
}

console.log(acumulator);

