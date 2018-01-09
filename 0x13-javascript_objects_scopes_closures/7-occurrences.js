#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c === undefined || c === '') {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
  exports.nbOccurences = function (list, searchElement) {
    for (let i = 0; i <= list; i++) {
      if (searchElement === list[i]) {
        let count += 1;
        print(count);
      }
    }
  }
}
const square = Square;
module.exports = square;
