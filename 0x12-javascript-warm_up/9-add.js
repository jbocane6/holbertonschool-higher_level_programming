#!/usr/bin/node
// Script that prints the addition of 2 integers.
// The first argument is the first integer.
// The second argument is the second integer.
// You have to define a function with this prototype: function add(a, b).
// You must use console.log(...) to print all output.
// You are not allowed to use var.
const { argv } = require('process');
const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);
function adding (a, b) { return a + b; }
console.log(adding(num1, num2));
