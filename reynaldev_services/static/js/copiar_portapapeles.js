/**
 * Created by Reynaldo on 14/07/2017.
 */

var audio = new Audio('/static/sound/sys_exchange_success.mp3');
var clipboard = new Clipboard('.clipboard');

clipboard.on('success', function(e) {
    Materialize.toast('Copiado!', 1000)
    audio.play()
});
clipboard.on('error', function(e) {
        console.log(e);
});