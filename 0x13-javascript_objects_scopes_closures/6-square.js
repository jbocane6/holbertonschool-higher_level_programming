#!/usr/bin/node
// Write a class Square that defines a square and inherits from Square of 5-square.js.
// You must use the class notation for defining your class and extends.
// Create an instance method called charPrint(c) that prints the rectangle using the character c.
// If c is undefined, use the character X.
const Rectangle = require('./4-rectangle');

// The constructor of Rectangle must be called (by using super()).
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const row = Array.apply([], Array(this.height));
    row.forEach(() => console.log(c.repeat(this.width)));
  }
}
module.exports = Square;
