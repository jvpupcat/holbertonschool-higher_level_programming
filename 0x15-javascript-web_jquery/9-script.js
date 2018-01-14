$(document).ready(function(){

  var $sf_wind_speed = $('#sf_wind_speed');

  $.ajax({
    type: 'GET',
    dataType: 'json',
    url: 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json',
    success: function(data) {
      const query = data.query;
      const results = query.results;
      const wind = results.channel.wind
      $sf_wind_speed.text(wind.speed);
    }
  });
});
