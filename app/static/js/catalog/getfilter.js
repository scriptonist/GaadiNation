 
 function sendData(filters) {
    console.log(filters);
    window.location = "/catalog/"+filters.join(",");
 }

$(document).ready(function(){

    var filters = Array();
    $('input:checkbox').click(function(){
        var id = $(this).attr('id');
        if($(this).attr('class') === "brand"){
            filters.push(JSON.stringify({"brand":id}));
        }

    });
     $('#apply_filter').click(function(){
        sendData(filters);
     });
      $('#apply_filter1').click(function(){
        sendData(filters);
     });
});