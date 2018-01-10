#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const URLarg = process.argv[2];
const filearg = process.argv[3];
request(URLarg, function(error, response, body){
  if (error) console.log(error);
  else {
    fs.writeFile(filearg, body, 'utf8', function (error) {
      if (error) console.log(error);
    });
  }
});
