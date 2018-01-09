#!/usr/bin/node
const arg = process.argv[2];
const fs = require('fs');
fs.readFile(arg, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
