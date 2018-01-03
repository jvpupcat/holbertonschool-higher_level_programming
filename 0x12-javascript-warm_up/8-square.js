#!/usr/bin/node
let arg = process.argv[2];
if (!arg) {
  console.log('Missing size')
} else {
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++) {
      console.log('X')
    }
  }
}
