$(document).ready(function(){
  $.getJSON('https://swapi.co/api/people/5/?format=json',
            {key, value}), function(data){
      $('#character').html(data.name);
    }
});
