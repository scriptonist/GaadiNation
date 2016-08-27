//query database to show ajax recomendations
// This uses an externam javascript library
$(document).ready(
    function() {
       
     $('#search_box_center_input').keyup(function() { 
    /* This function will run on every keyup event on the
       search box in in the landing page
     */
     query = $('#search_box_center_input').val();
         if (query) {
             var options = {
              url: function(query) {
                  return "search/" + query; // The api endpoint
              },

              getValue: "carname" ,// The key whose value to be extracted
              list: {
                  showAnimation: {
                      type: "fade", //normal|slide|fade
                      time: 400,
                      callback: function() {}
                  },

                  hideAnimation: {
                      type: "slide", //normal|slide|fade
                      time: 400,
                      callback: function() {}
                  }
              }

        };

          $("#search_box_center_input").easyAutocomplete(options); // Register the element with autocomplete

         }
     });
     });

