#!/usr/bin/node
const FileArg = process.argv[2];
const LineArg = process.argv[3];
const fs = require('fs');
fs.writeFile(FileArg, LineArg, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
