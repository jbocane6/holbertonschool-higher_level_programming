#!/usr/bin/node
// Write a script that display the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code must be printed like this: code: <status code>
// You must use the module request

// Require https which includes get() function
const https = require('https');
https.get(process.argv[2], function (res) {
  console.log('code: ', res.statusCode);
});
