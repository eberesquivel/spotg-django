/**
 * Created by Reynaldo on 19/07/2017.
 */
function setCookie(nombre, valor)
{
    Cookies.set(nombre, valor, {expires: 2});
}

function leerCookie(nombre)
{
    var modal_youtube = Cookies.get(nombre);
    if( modal_youtube == null)
        return false;
    return true;
}

$(document).ready(function()
{
    if (leerCookie('modal_youtube'))
        return;

    $('#modal-youtube').modal('open');

});