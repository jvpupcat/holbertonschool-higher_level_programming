#!/usr/bin/node
let arg = process.argv[2];
if (!arg || isNaN(arg)) {
  console.log('Missing size');
}
for (let i = 0; i < arg; i++) {
  console.log('X'.repeat(arg));
}
