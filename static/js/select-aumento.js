/**
 * Created by Reynaldo on 13/07/2017.
 */

function cambiarContenidoTabla() {
    var animacion = "animated flash";
    var imagen_activo = $('#img-active');
    var imagen_chance = $('#img-chance');
    var imagen_pasivo = $('#img-passive');
    var animation_end = "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";

    var valor_seleccionado = $('#select-aumento').val();
    var todos = $('#aumentos-todos');
    var activos = $('#aumentos-activos');
    var chances = $('#aumentos-chances');
    var pasivos = $('#aumentos-pasivos');

    if( valor_seleccionado == "todos")
    {
        todos.removeClass('hide');
        activos.addClass('hide');
        chances.addClass('hide');
        pasivos.addClass('hide');
    }
    else if (valor_seleccionado == "activos")
    {
        activos.removeClass('hide');
        todos.addClass('hide');
        chances.addClass('hide');
        pasivos.addClass('hide');

        // Agrega la animacion usando addClass
        imagen_activo.addClass(animacion).one(animation_end, //Segundo parametro de ".one" es una funcion
                                                                        function () {
                                                                            $(this).removeClass(animacion)
                                                                        });
    }
    else if (valor_seleccionado == "chances")
    {
        chances.removeClass('hide');
        todos.addClass('hide');
        activos.addClass('hide');
        pasivos.addClass('hide');

        // Agrega la animacion usando addClass
        imagen_chance.addClass(animacion).one(animation_end, //Segundo parametro de ".one" es una funcion
                                                                        function () {
                                                                            $(this).removeClass(animacion)
                                                                        });
    }
    else if (valor_seleccionado == "pasivos")
    {
        pasivos.removeClass('hide');
        todos.addClass('hide');
        activos.addClass('hide');
        chances.addClass('hide');

       // Agrega la animacion usando addClass
        imagen_pasivo.addClass(animacion).one(animation_end, //Segundo parametro de ".one" es una funcion
                                                                        function () {
                                                                            $(this).removeClass(animacion)
                                                                        });
    }

    $('#mostrando').text(valor_seleccionado);
}