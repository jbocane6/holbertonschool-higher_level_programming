#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
// The first argument is the API URL:https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
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
    const results = JSON.parse(values);
    const completed = {};
    // Move through the results
    for (const result of results) {
      if (result.completed) {
        if (completed[result.userId]) {
          completed[result.userId] += 1;
        } else {
          completed[result.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
