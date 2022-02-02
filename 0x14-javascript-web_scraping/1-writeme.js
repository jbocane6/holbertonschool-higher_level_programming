#!/usr/bin/node
// Write a script that writes a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object

// Require fs which includes writefile() function
const fs = require('fs');
// fs requires to write file the 2nd arg, the 1st is the node file
// and the 3rd arg is the text to copy
fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});
