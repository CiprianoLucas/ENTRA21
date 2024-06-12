//Escreva a função sumSalaries(salaries)que retorna a soma de todos os salários usando Object.valuese o for..ofloop.

const sumSalaries = (obj) => {

    let acumulator = 0
    for(let value of Object.values(obj)){
        acumulator += value
    }
    return acumulator
}

let salaries = {
    "John": 100,
    "Pete": 300,
    "Mary": 250
  };

  console.log( sumSalaries(salaries) ); // 650

//Escreva uma função count(obj)que retorne o número de propriedades do objeto:

const count = (obj) => {
    return Object.keys(obj).length
}

let user = {
    name: 'John',
    age: 30
  };
  
  console.log( count(user) ); // 2

