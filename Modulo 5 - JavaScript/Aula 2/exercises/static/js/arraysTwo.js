//Escreva a função getAverageAge(users)que obtém um array de objetos com propriedade agee retorna a idade média.

/**
 * Calcula a idade média com base em um array de objetos com a propriedade 'age'.
 *
 * @param {Array} users - O array de objetos contendo as idades.
 * @returns {number} - A idade média.
 */
const getAverageAge = (users) => {
    if (users.length === 0) {
      return 0;
    }
  
    const averageAge = users.reduce((total, user) => total + user.age, 0)/users.length;
  
    return averageAge;
  }
  
  let john = { name: "John", age: 25 };
  let pete = { name: "Pete", age: 30 };
  let mary = { name: "Mary", age: 29 };
  
  let arr = [john, pete, mary];
  
  console.log(getAverageAge(arr));



//Escreva uma função filterRange(arr, a, b)que obtenha um array arr, procure elementos com valores maiores ou iguais ae menores ou iguais be retorne um resultado como um array.

  /**
 * Filtra uma array com base no valor base e máximo
 * @param {Array} args - Array a ser filtrado
 * @param {Number} a - Menor valor
 * @param {Number} b - Maior valor
 * @returns {Array} - Array filtrado
 */
const filterRange = (args, a, b) => {
    return args.filter(item => item >= a && item <= b);
}

let args = [1,2,4,5,6,8,9,11];
let filtered = filterRange(args, 2, 8);
console.log(filtered);

//Classifique em ordem decrescente

let arguments = [5, 2, 1, -10, 8];

arguments.sort((a,b) => b-a)

console.log( arguments ); // 8, 5, 2, 1, -10
