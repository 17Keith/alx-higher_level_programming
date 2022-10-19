#!/usr/bin/node

// Prints the number of movies where a character is present.

const request = require('request');

request(process.argv[2], (error, _response, body) => {
  if (error) {
    console.log(error);
  } else {
    const _response = JSON.parse(body).results.filter(item => item.characters.find(id => id.match(/18/)));
    console.log(_response.length);
  }
});
