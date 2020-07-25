/**
 * Created by Reynaldo on 27/06/2017.
 */
/* Metodo para donar */
$('#donar').click(function(){
    var cantidad = document.getElementById('cantidad').value;
    var moneda = document.getElementById("moneda").value;

    if (cantidad == "")
    {
        cantidad = 5;
    }

    window.location.href = "https://www.paypal.me/EberEsquivel/" + cantidad + moneda;
    return false;
});