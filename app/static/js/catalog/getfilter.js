 var filters = {"brand":[]};
 function sendData() {

    $.ajax({
        url: '/catalog/',
        type: 'POST',
        data: JSON.stringify(filters),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: true,
        success: function(content) {
            console.log(content);
        }
    });
 }

$(document).ready(function(){


    $('input:checkbox').click(function(){
        var id = $(this).attr('id');
        if($(this).attr('class') === "brand"){
            filters.brand.push(id);
            console.log(filters);

        }

    });
     $('#apply_filter').click(function(){
        sendData();
     });
      $('#apply_filter1').click(function(){
        sendData();
     });
});