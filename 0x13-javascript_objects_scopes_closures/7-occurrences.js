#!/usr/bin/node
// Write a function that returns the number of occurrences in a list.
// Prototype: exports.nbOccurences = function (list, searchElement).
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    counter = searchElement === list[i] ? counter + 1 : counter;
  }
  return counter;
};
