#!/usr/bin/node
module.exports.esrever = function (list) {
  let reverse = new Array;
    for (let i = 0; i <= list; i--) {
      reverse.push(list[i])
    }
  return reverse;
}
