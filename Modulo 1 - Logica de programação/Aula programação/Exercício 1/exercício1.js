function calcular (peso, altura, parametro){

    if(typeof peso !== "number" || typeof altura !== "number"){
        return ("Um ou mais valores não são números")
    }

    if(typeof parametro === "function"){
        return parametro()
    }

return peso/(altura*altura)

    IMC = (peso/(altura*altura))

    if(IMC<16.9){
        return("Peso muito abaixo do ideal")
    }
    else if(IMC < 30){
        return ("ta ok")
    }
    else{
        return ("Tu vai morrer")
    }

}

console.log(calcular(100))

function UmaFn () {
    return "Pq você me chamou?"
}
