#!/usr/bin/node
const request = require('request');
const arg = process.argv[2];
request(arg, function (error, response, body) {
  if (error) console.log(error);
  else {
    console.log(JSON.parse(body).endsWith(18));
  }
});
