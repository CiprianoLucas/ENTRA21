
//Crie um contador usando jQuery adicione a funcionalidade de incrementar e decrementar.

$(document).ready(() => {

    const $buttonPauseResume = $("#pauseResume")
    const $buttonReset = $("#reset")
    const $cronometer = $("p")

    let setCronometer
    let seconds = 0
    let minutes = 0
    let hours = 0


    let isResume = false

    /**
     * Faz a atualização do cronômetro adicionando um segundo
     */
    const updateCronometer = () => {
        seconds = seconds += 1
        if (seconds >= 60) {
            seconds = 0;
            minutes += 1;
        }
        if (minutes >= 60) {
            minutes = 0;
            hours += 1;
        }

        $cronometer.text(`${String(hours).padStart(2, "0")}:${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`)

    }


    /**
     * Alterna entre pausar e resumir o cronômetro
     */
    const alternatePauseResume = () => {
        isResume = !isResume

        if (isResume) {
            $buttonPauseResume.text("Pausar")
            setCronometer = setInterval(updateCronometer, 1000);
        }
        else {
            $buttonPauseResume.text("Resumir")
            clearInterval(setCronometer);
        }
    }

    /**
     * Faz o reset do cronômetro
     */
    const resetCronometer = () => {
        seconds = 0
        minutes = 0
        hours = 0
        $cronometer.text("00:00:00")
    }




    $buttonPauseResume.click(alternatePauseResume)
    $buttonReset.click(resetCronometer)

}) 
