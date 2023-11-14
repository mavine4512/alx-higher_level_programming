#!/usr/bin/node

exports.converter = function (base) {
  function myConverter (n) {
    return n.tostring(base);
  }

  return myConverter;
};
