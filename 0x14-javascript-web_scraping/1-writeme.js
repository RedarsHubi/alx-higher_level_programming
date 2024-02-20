#!/usr/bin/node
const fs = require('fs');
contento = process.argv[3]
fs.writeFile(process.argv[2], contento, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
