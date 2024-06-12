
//Crie um contador usando jQuery adicione a funcionalidade de incrementar e decrementar.

$(document).ready(()=> {
    
const $p = $("p")
const $plus = $("#plus")
const $subtract = $("#subtract")

let counter = 0;

const plusCounter = () => {
    counter += 1;
    $p.text(counter)
}

const subtractCounter = () => {
    counter -= 1;
    $p.text(counter)
}

$plus.click(plusCounter)
$subtract.click(subtractCounter)
}) 
