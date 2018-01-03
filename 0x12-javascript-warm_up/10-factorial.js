#!/usr/bin/node
let num = parseInt(process.argv[2]);
function factorialize (num) {
  if (!num) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}
console.log(factorialize(num));
