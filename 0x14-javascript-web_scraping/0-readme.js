#!/usr/bin/node

"Script that readss and prints the content of a file"

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, result) {
    if (err) {
        console.log(err);
    } else {
        console.log(result);
    }
});