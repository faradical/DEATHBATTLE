// Stick Figure Functions-------------------------------------------------------
function BuildStickFigure1(name){
    
    var queryUrl = 'https://www.superheroapi.com/api.php/10220306273917389/'
    var url = queryUrl + name; 

    d3.json(url, function(response){

      var height_1 = parseFloat(response.appearance.height[1])* 10;

      var api_red_height_actual_height = height_1;


      var default_red_height_actual_height = 1500;


      var default_red_image_height = 150;


      var api_red_height_image_height = (api_red_height_actual_height) * default_red_image_height / default_red_height_actual_height;

      d3.select("#idLeft").attr("height", api_red_height_image_height);

    console.log(api_red_height_actual_height);
    })

    
}


function BuildStickFigure2(name){
    
  var queryUrl = 'https://www.superheroapi.com/api.php/10220306273917389/'
  var url = queryUrl + name; 

  d3.json(url, function(response){

    var height_1 = parseFloat(response.appearance.height[1])* 10;

    var api_blue_height_actual_height = height_1;

    var default_blue_height_actual_height = 1500;

    var default_blue_image_height = 150;

    var api_blue_height_image_height = (api_blue_height_actual_height) * default_blue_image_height / default_blue_height_actual_height; 

    d3.select("#idRight").attr("height", api_blue_height_image_height);
    
  console.log(api_blue_height_actual_height);
  })
  
}

BuildStickFigure1("209");
BuildStickFigure2("332");