 compare = Array();
    $('.addToCompare').click(function(){
        if(compare.length < 4){
                if($.inArray($(this).attr('id'),compare) == -1){
                    compare.push($(this).attr('id'));
                    Materialize.toast('Car Added to Compare List', 1000,'rounded')
                }
                else{
                    compare.splice( $.inArray($(this).attr('id'),compare) ,1 );
                    Materialize.toast('Car Removed from Compare List', 1000,'rounded')
                }
            }
        else
            Materialize.toast('You Can Only Compare 4 Cars at a time', 1000,'rounded')
        console.log(compare);
    });
    $('#compareButton').click(function(){
        window.location = "/compare/compare_display/"+compare.join(',');
    });