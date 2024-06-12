/*
Escreva uma função formatDate(date)que deve ser formatada dateda seguinte forma:
Se desde então datepassou menos de 1 segundo, então "right now".
Caso contrário, se datepassou menos de 1 minuto, então "n sec. ago".
Caso contrário, se for menos de uma hora, então "m min. ago".
Caso contrário, a data completa no formato "DD.MM.YY HH:mm". Ou seja: "day.month.year hours:minutes", tudo em formato de 2 dígitos, por exemplo 31.12.16 10:00.
*/


/**
 * Formata uma data
 * @param {Date} date - A data a ser formatada.
 * @returns {string} - A data formatada de acordo com as regras especificadas.
 */
const formatDate = (date) => {
    const now = new Date();
    const diff = now - date;
  
    if (diff < 1000) {
      return "right now";
    } 
    else if (diff < 60000) {
      const seconds = Math.floor(diff / 1000);
      return `${seconds} sec. ago`;
    } 
    else if (diff < 3600000) {
      const minutes = Math.floor(diff / 60000);
      return `${minutes} min. ago`;
    }
    else if (diff < 86400000){
        const hours = Math.floor(diff / 3600000);
        return `${hours} hours. ago`;
    }
    else {
      const day = String(date.getDate()).padStart(2, '0');
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const year = String(date.getFullYear()).slice(-2);
      const hours = String(date.getHours()).padStart(2, '0');
      const minutes = String(date.getMinutes()).padStart(2, '0');
  
      return `yesterday's date like ${day}.${month}.${year} ${hours}:${minutes}`;
    }
  }
  
console.log( formatDate(new Date(new Date - 1)) ); // "right now"
console.log( formatDate(new Date(new Date - 30 * 1000)) ); // "30 sec. ago"
console.log( formatDate(new Date(new Date - 5 * 60 * 1000)) ); // "5 min. ago"
console.log( formatDate(new Date(new Date - 7* 60 * 60 * 1000)) ); // "7 hours. ago"
console.log( formatDate(new Date(new Date - 86400 * 1000)) ); // yesterday's date like 31.12.16 20:00


//Escreva uma função getLastDayOfMonth(year, month)que retorne o último dia do mês. Às vezes é 30, 31 ou até 28/29 de fevereiro.
const getLastDateOfMonth = (year, month) => new Date(year, month + 1, 0).getDate();

console.log(getLastDateOfMonth(2023,2))


//Escreva uma função getSecondsToday()que retorne o número de segundos desde o início de hoje.


/**
 * Retorna o número de segundos desde o início de hoje.
 *
 * @returns {number} - O número de segundos desde o início do dia atual.
 */
const getSecondsToday = () => {
    const time = new Date();
    const startDay = new Date(time.getFullYear(), time.getMonth(), time.getDate());
  
    return Math.floor((time - startDay) / 1000);
  }

console.log(getSecondsToday())