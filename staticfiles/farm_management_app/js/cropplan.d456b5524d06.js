// function myFunction() {
//     alert("Hello from a static file!");
//   }




function checkChange(){
    console.log("changed")
    let location_select = document.getElementById('div_id_location');

    console.log(location_select)
    if (location_select != null){
        console.log(location_select.name)


        let beds = document.getElementById('id_beds').options;
        // console.log(beds.0)
        console.log("beds",beds)
        console.log("hello2")
    }
}

$("#id_location").change(function () {
    var url = $("#personForm").attr("data-cities-url");  // get the url of the `load_cities` view
    var countryId = $(this).val();  // get the selected country ID from the HTML input

    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'country': countryId       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_city").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });


console.log("hello")