#!/usr/bin/node
// Script that computes and prints a factorial.
// The first argument is integer (argument can be cast as integer) used for computing the factorial.
// Factorial of NaN is 1.
// You must do it recursively.
// You must use a function.
// You must use console.log(...) to print all output.
// You are not allowed to use var.
const { argv } = require('process');
const num1 = parseInt(argv[2]);
console.log(factorial(num1));
function factorial (num1) {
  if (num1 === 0 || isNaN(num1)) {
    return 1;
  } else {
    return num1 * factorial(num1 - 1);
  }
}
