#!/usr/bin/node

// Script that displays status code of a GET request

const request = require('request');

request(process.argv[2], function (error, response) {
  if (error) {
    console.log(error);
  }
  console.log('code:', response && response.statusCode);
});
