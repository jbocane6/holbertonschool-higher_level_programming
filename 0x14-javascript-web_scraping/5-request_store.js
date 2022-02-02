#!/usr/bin/node
// Write a script that gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file must be UTF-8 encoded
// You must use the module request

// Require request which includes put() function
const request = require('request');
// Require fs which includes writefile() function
const fs = require('fs');
request(process.argv[2], (error, response, values) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], values, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
