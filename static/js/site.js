/**
 * Created by Reynaldo on 26/06/2017.
 */
$(document).ready(function() {
    $('select').material_select();
    $('.carousel').carousel();
    setInterval(function() {
        $('.carousel').carousel('next');
    }, 10000);
    /* Poner debajo las opciones al darle clic al DropDown */
    $(".dropdown-button").dropdown({
        belowOrigin: true, // Displays dropdown below the button
    });
    /*Boton ir arriba */
    $('#btn-ir-arriba').click(function(){
		$('html, body').animate({scrollTop : 0},800);
		return false;
	});
    $('.slider').slider();
});

/* Metodos para ir arriba */
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200)
    {
        $("#btn-ir-arriba").fadeIn();
    }
    else
    {
        $("#btn-ir-arriba").fadeOut();
    }
}

$('#fb-msgr').hover(function () {
  $(this).toggleClass('rubberBand');
});


$('#boton-nav').hover(function () {
    $(this).toggleClass('rubberBand');
  });

  $('#intro').hover(function () {
    $(this).toggleClass('rubberBand');
  });

  $('#acerca').hover(function () {
    $(this).toggleClass('tada');
  });

  $('#proyectos').hover(function () {
    $(this).toggleClass('rubberBand');
  });

  $('#angular').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#queso').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#flask').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#chatnode').hover(function () {
    $(this).toggleClass('rubberBand');
  });

  $('#domotica').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#bomba').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#mapa').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#domo').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#cabecera1').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#phaser').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#portafolio').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#aventura').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#axe').hover(function () {
    $(this).toggleClass('rubberBand');
  });
  $('#atomo').hover(function () {
    $(this).toggleClass('bounce');
  });
  $('#atomomenu').hover(function () {
    $(this).toggleClass('tada');
  });