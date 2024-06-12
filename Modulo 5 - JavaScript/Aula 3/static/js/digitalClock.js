$(document).ready(() => {

// Selecionando os elementos do DOM
const $clock = $(".clock");
const $date = $(".date");
const $button = $("#toggleButton");

/**
 *Atualiza o relógio
 */
const updateClock = () => $clock.text(new Date().toLocaleTimeString());

/**
 * Formata o dia da semana de número para o formato português
 * @param {number} dayOfWeek - Dia da semana 
 * @returns {string} dia da semana formatado
 */
const formatDayOfWeek = (dayOfWeek) => {
    const daysOfWeek = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"];
    return daysOfWeek[dayOfWeek];
};

/**
 * Formata o mês de número para português
 * @param {number} month - número do mês 
 * @returns {string} dia do mês formatado
 */
const formatMonth = (month) => {
    const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
    return monthNames[month];
};

/**
 * Formata o dia do mês para que ele sempre possua duas casas
 * @param {number} day - dia do mês
 * @returns {string} dia do mês com duas casas
 */
const formatDay = (day) => String(day).padStart(2, "0");

/**
 * Atualiza a data
 */
const updateDate = () => {
    const today = new Date();
    const dayOfWeek = formatDayOfWeek(today.getDay());
    const month = formatMonth(today.getMonth());
    const day = formatDay(today.getDate());
    const year = today.getFullYear();

    $date.text(`${dayOfWeek}, ${day} de ${month} de ${year}`);
};

let isPaused = false
let clockTimer = setInterval(updateClock, 500);

/**
 * Função para parar ou retomar o relógio
 */
const toggleTimer = () => {
    isPaused = !isPaused;

    if (isPaused) {
        clearInterval(clockTimer);
        $button.text("Resumir")
        $button.css("background-color", "#ADE25D")

    }
    else {
        clockTimer = setInterval(updateClock, 500);
        $button.text("Pausar")
        $button.css("background-color", "rgb(6, 164, 236)")
    }
}

$button.click(toggleTimer);


updateClock();
updateDate();
})