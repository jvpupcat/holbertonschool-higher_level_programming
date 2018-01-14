$(function (){

  var $list_movies = $('#list_movies');

  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'https://swapi.co/api/films/?format=json',
    success: function(data) {
      $.each(data), function(i, item) {
        $data.append('<li>item.title</li>');
      }
    }
  })
});
