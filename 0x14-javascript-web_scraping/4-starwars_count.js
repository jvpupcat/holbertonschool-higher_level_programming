#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = (JSON.parse(body).results);
    for (let i = 0; results != NULL; i++) {
      if (results[i] === 'characters') {
        for (let j = 0; j < characters; j++) {
          if (characters[j] === '1' && characters[j + 1] === '8') {
            console.log(results.character)
          }
        }
      }
    }
  }
});
