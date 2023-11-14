#!/usr/bin/node
/**
 * Square class that inherits from rectangle class
 */
const Reactangle = require('./4-rectangle');

class Square extends Reactangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
