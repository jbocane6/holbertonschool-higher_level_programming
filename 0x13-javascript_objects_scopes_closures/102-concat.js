#!/usr/bin/node
// Write a script that concats 2 files.
// The first argument is the file path of the first source file.
// The second argument is the file path of the second source file.
// The third argument is the file path of the destination.
let { argv } = require('process');
const fs = require('fs');

argv = argv.slice(2);
const argc = argv.length;

if (argc === 3) {
  const fileA = fs.readFileSync(argv[0]);
  const fileB = fs.readFileSync(argv[1]);
  fs.writeFileSync(argv[2], fileA + fileB);
}
