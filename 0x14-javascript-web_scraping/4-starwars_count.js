#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
const characterID = 'http://swapi.co/api/people/18/';
request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let resultsize = JSON.parse(body).results.length;
    let count = 0;
    for (let i = 0; i < resultsize; i++) {
      if (JSON.parse(body).results[i].characters === characterID) {
        count++;
      }
    }
    console.log(count);
  }
});
