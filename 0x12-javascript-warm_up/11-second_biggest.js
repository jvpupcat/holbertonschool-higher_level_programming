#!/usr/bin/node
let arg1 = process.argv[2]
let arg2 = process.argv[3]
let all_args = [];
if (!arg1 || !arg2) {
  console.log('0');
} else {
  for (let i = 0; i < process.argv[i]; i++) {
    all.sort.push(process.argv[i]);
  }
  second_largest = all_args.length - 2;
  console.log(all_args[second_largest]);
}
