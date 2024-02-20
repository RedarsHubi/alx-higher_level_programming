#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
let occ = 0;

request(url, function (error, response, body) {
  if (error == null) {
    const movie = JSON.parse(body);
    const results = movie.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          occ++;
        }
      }
    }
  }
  console.log(occ);
});
