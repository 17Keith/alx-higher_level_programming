#!/usr/bin/node

// prints the name of Starwars characters in no particular order.

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, _response, body) {
  if (error) {
    console.error(error);
  }
  JSON.parse(body).characters.forEach(function (url, _callback) {
    request(url, function (error, _response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
