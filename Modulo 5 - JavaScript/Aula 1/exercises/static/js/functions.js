//Escreva uma função pow(x,n)que retorne xem potência n. Ou, em outras palavras, multiplica xpor si mesmo ne retorna o resultado.

function pow(base, exponent){
    let acumulator = 1
    for(let i = 0; i < exponent; i++){
        acumulator *= base
    }
    return acumulator
}

alert(pow(3,3))