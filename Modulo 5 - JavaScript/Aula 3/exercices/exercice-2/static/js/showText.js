//Desabilite a funcionalidade do botão direito em uma página utilizando jQuery.

const $button = $("#clicker");
const $p = $("#secret")

let isShow = false

const showText = () => {
    isShow = !isShow
    $p.css("display", isShow ? "inline" : "none")
}

$button.click(showText);
$(document).on('contextmenu', function() { return false;});

