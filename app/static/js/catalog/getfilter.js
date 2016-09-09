$(document).ready(function(){
    var filtert = {"cars":[]};
    $('input:checkbox').click(function(){
        var id = $(this).attr('id');
        console.log(id);
    });
});