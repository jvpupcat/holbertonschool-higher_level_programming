#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h)) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    let twoxh = 2 * this.height;
    let twoxw = 2 * this.width;
    for (let j = 0; j < twoxw; j++) {
      console.log('X'.repeat(twoxh))
    }
  }
  double () {
    let twoxh = 2 * this.height;
    let twoxw = 2 * this.width;
    for (let k = 0; k < twoxh; k++)
      console.log('X'.repeat(twoxw))
  }
};
const rectangle = Rectangle;
module.exports = rectangle;
