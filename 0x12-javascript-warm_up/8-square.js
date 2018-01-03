#!/usr/bin/node
let arg = process.argv[2];
let x = 'X';
if (!arg) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log(x.repeat(arg));
  }
}
