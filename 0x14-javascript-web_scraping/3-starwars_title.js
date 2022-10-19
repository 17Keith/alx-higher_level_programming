#!/usr/bin/node

// Prints the tittle of a Star Wars movie.

const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, _response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
