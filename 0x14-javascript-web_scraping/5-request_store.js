#!/usr/bin/node

// Script that gets content of a webpage

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  try {
    fs.writeFile(process.argv[3], body, 'utf8', function (error, result) {
      if (error) console.log(error);
    });
  } catch (error) {
    console.log(error);
  }
});
