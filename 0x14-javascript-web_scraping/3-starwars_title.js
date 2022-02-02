#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie
// where the episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint
// https://swapi-api.hbtn.io/api/films/:id
// You must use the module request

// Require request which includes put() function
const request = require('request');
// To request, we need to concatenate the api with the endpoint
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, values) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(values).title);
  }
});
