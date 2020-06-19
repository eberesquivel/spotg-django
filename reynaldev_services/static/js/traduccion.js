/**
 * Created by Reynaldo on 02/07/2017.
 */
$(document).ready(function() {
    $('#lenguaje-es').click(function(){
        postLang("es");
        return false;
	});
    $('#mobile-lenguaje-es').click(function(){
        postLang("es");
        return false;
	});
    $('#lenguaje-en').click(function(){
        postLang("en");
        return false;
	});
    $('#mobile-lenguaje-en').click(function(){
        postLang("en");
        return false;
	});
});

function postLang(lenguaje){
   document.getElementById("lenguaje-seleccionado").value = lenguaje;
   document.getElementById("form-lenguaje").submit();
}