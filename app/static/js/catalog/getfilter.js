brands = Array();
price  = Array();
bodytype = Array();

$('.brand').click(function(){
  if($(this).is(":checked")){
    brands.push($(this).val())
    
  }
  else{
    var removeItem = $(this).val();

    brands = jQuery.grep(brands, function(value) {
    return value != removeItem;
    });
  }
 $("input[id=brand_input_box]").attr("value",brands.join(","));
  
});

$('.price').click(function(){

  if($(this).is(":checked")){
    price.push($(this).val())
    
  }
  else{
    var removeItem = $(this).val();

    price = jQuery.grep(price, function(value) {
    return value != removeItem;
    });
  }
 $("input[id=price_input_box]").attr("value",price.join(","));
  
});

$('.bodytype').click(function(){
  if($(this).is(":checked")){
    bodytype.push($(this).val())
    
  }
  else{
    var removeItem = $(this).val();

    bodytype = jQuery.grep(bodytype, function(value) {
    return value != removeItem;
    });
  }
 $("input[id=bodytype_input_box]").attr("value",bodytype.join(","));
  
});

var fl = 1;
$("#showmorebutton").click(function(){
  if(fl === 1){
    $('#hidden_brands').removeClass('hide');
    $(this).html("show less");
    fl = 0;
  }
  else{
    fl = 1;
    $('#hidden_brands').addClass('hide');
    $(this).html("show more");
  }
});