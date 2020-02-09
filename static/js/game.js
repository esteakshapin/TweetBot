$(document).ready(function(){
      $('#startGameButton').click(function() {
        $.post('/startGame', {
        }).done(function() {
            document.location.reload();
        });
    });
});