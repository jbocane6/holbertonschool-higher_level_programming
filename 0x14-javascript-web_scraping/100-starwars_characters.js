#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line
// You must use the Star wars API
// You must use the module request

// Require request which includes put() function
const request = require('request');
// To request, we need to concatenate the api with the endpoint
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, values) => {
  if (error) {
    console.log(error);
  } else {
    // Store the results
    const results = JSON.parse(values).characters;
    for (const result of results) {
      // as results contains a list of urls we request each one of them
      request(result, (error, response, values) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(values).name);
        }
      });
    }
  }
});
