/**
 * Created by Reynaldo on 11/07/2017.
 */
// Deshabilita el clic derecho
document.oncontextmenu = function(){return false;};
// Deshabilita el seleccionar
document.onselectstart = function(){return false;};
// Deshabilita el arrastrar
document.ondragstart = function(){return false;};

/* Las siguientes lineas usan la libreria jquery.hotkeys */
/* Ver ejemplos https://rawgit.com/jeresig/jquery.hotkeys/master/test-static-01.html */

// Deshabilita Control + F10
$(document).on('keydown', null, 'f10', function(){
   return false;
});

// Deshabilita Control + F12
$(document).on('keydown', null, 'f12', function(){
   return false;
});

// Deshabilita Control + S
$(document).on('keydown', null, 'ctrl+s', function(){
   return false;
});
// Deshabilita Control + A
$(document).on('keydown', null, 'ctrl+a', function(){
   return false;
});

// Deshabilita Control + F
//$(document).on('keydown', null, 'ctrl+f', function(){
//   return false;
//});

// Deshabilita Control + P
$(document).on('keydown', null, 'ctrl+p', function(){
   return false;
});

// Deshabilita Control + u, sirve para ver código fuente de la página
$(document).on('keydown', null, 'ctrl+u', function(){
   return false;
});

// Deshabilita Control + u, sirve para ver código fuente de la página
$(document).on('keydown', null, 'ctrl+u', function(){
   return false;
});

// Deshabilita Control + shift + c, sirve para inspeccionar elemento con el mouse
$(document).on('keydown', null, 'ctrl+shift+c', function(){
   return false;
});

// Deshabilita Control + shift + i, sirve para inspeccionar elemento
$(document).on('keydown', null, 'ctrl+shift+i', function(){
   return false;
});

// Deshabilita Control + shift + j, sirve para abrir la consola
$(document).on('keydown', null, 'ctrl+shift+j', function(){
   return false;
});