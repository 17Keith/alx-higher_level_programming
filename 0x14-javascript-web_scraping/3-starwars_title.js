#!/usr/bin/node

// Prints the tittle of a Star Wars movie.

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/'+ process.argv[2], function (error,  body) {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
