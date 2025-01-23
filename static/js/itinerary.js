$(document).ready(function () {
    $('#div1').show();

    $('.showSingle').click(function () {
        $('.targetDiv').hide();
        $('#div' + $(this).attr('target')).show();
    });

});



