#!/usr/bin/node
// Write a script that prints the number of movies where the character
// “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars
// API: https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character ID 18 - your script must use this ID
// for filtering the result of the API
// You must use the module request

// Require request which includes put() function
const request = require('request');
// To request, we need the api
const url = process.argv[2];
request(url, (error, response, values) => {
  if (error) {
    console.log(error);
  } else {
    // Store the results
    const titles = JSON.parse(values).results;
    let counter = 0;
    // Move through the results
    for (const title of titles) {
      // if contains 18, adds 1
      if (title.characters.find((character) => character.includes('18'))) {
        counter += 1;
      }
    }
    console.log(counter);
  }
});
