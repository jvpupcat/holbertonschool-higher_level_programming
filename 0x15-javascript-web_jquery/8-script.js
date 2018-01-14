$(document).ready(function (){

  var $list_movies = $('#list_movies');

  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'https://swapi.co/api/films/?format=json',
    success: function(data) {
      const results = data.results;
      $.each(results, function(i, item) {
        $list_movies.append('<li>' + item.title + '</li>');
      }
    });
  });
});
