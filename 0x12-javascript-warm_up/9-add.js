#!/usr/bin/node
let a = process.argv[2];
let b = process.argv[3];
function add(a, b) {
  if (!a || !b) {
    return NaN;
  } else {
      return a + b;
  }
}
console.log(a + b);
