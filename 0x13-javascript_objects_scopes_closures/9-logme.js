#!/usr/bin/node
/* Write a function that prints the number of arguments already printed.
and the new argument value.
prototype: exports.logMe = function (item).
Output format: <number arguments already printed>: <current argument value></current>. */
let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter += 1;
};
