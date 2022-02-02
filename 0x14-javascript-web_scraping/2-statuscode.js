#!/usr/bin/node
// Write a script that display the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>
// You must use the module request

// Require https which includes get() function
const request = require('request');
request(process.argv[2], (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
