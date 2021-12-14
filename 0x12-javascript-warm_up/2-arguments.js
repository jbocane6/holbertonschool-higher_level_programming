#!/usr/bin/node
// Script that prints a message depending of the number of arguments passed.
// If no arguments are passed to the script, print “No argument”.
// If only one argument is passed to the script, print “Argument found”.
// Otherwise, print “Arguments found”.
// You must use console.log(...) to print all output.
// You are not allowed to use var.

const { argv } = require('process');
const argc = argv.length - 2;
if (argc === 0) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else if (argc > 1) {
  console.log('Arguments found');
}
