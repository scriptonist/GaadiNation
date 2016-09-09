$(document).ready(function(){
    var filters = {"brand":[]};
     function sendData() {
            $.ajax({
                url: "/catalog/",
                type: 'POST',
                 contentType: 'application/json',
                data: { json: JSON.stringify(filters)
                 },
                dataType: 'json'
            });
     }

    $('input:checkbox').click(function(){
        var id = $(this).attr('id');
        if($(this).attr('class') === "brand"){
            filters.brand.push(id);
            console.log(filters);
            sendData();
        }

    });
});