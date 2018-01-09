#!/usr/bin/node
const request = require('request');
const arg = process.argv[2]
const StarWarsURL = 'http://swapi.co/api/films/' + arg
request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title)
  }
});
