/**
 * Created by Reynaldo on 11/07/2017.
 */
function actualizarHora() {
    var hora = $('#hora').text();
    hora = parseInt(hora);
    var minuto = $('#minuto').text();
    minuto = parseInt(minuto);
    var segundo = $('#segundo').text();
    segundo = parseInt(segundo);
    segundo++;


    if (segundo == 60)
    {
        minuto++;
        segundo = 0;
        if(minuto == 60)
        {
            minuto = 0;
            hora++;

            if(hora == 24)
                hora = 0;

            if(hora <= 9)
                hora = "0" + hora;

            $('#hora').text(hora)
        }

        if (minuto <= 9)
            minuto = "0" + minuto;

        $('#minuto').text(minuto)
    }

    if (segundo <= 9)
        segundo = "0" + segundo;

    $('#segundo').text(segundo);

}

setInterval(actualizarHora, 1000)