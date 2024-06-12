$(document).ready(function() {

    const $gridsItem = $(".grid-item")
    const $p = $("p")

    /**
     * Irá marcar o objeto selecionado e tirar marcação do objeto anterior
     */
    const atualizateSelect = () => {   
        let numeroQuadrado = $(event.target).text();

        $gridsItem.removeClass("selected");
        $(event.target).addClass("selected");
        $p.text("Quadrado selecionado: " + numeroQuadrado);
    }

    $gridsItem.click(atualizateSelect);
});

