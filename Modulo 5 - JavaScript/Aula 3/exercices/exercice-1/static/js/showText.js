//Utilizando jQuery faça com que seja possível mostrar/esconder o <p>. O texto do botão deve ser alterado também (“mostrar” ou “esconder”).


const $button = $("#clicker");
const $p = $("#secret")

let isShow = false

const showText = () => {
    isShow = !isShow
    $p.css("display", isShow ? "inline" : "none")
}

$button.click(showText);
