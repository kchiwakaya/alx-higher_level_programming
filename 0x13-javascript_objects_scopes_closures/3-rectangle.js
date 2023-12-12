#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a;
    let b;
    let build = '';
    for (a = 0; a < this.height; a++) {
      if (a > 0) {
        build += '\n';
      }
      for (b = 0; b < this.width; b++) {
        build += 'X';
      }
    }
    console.log(build);
  }
}
module.exports = Rectangle;
