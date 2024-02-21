#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(url, function (error, response, body) {
  if (error == null && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const cara = movie.characters;
    function getcara (cara) {
      request(cara, function (error, response, body) {
        if (error == null) {
          console.log(JSON.parse(body).name);
        }
      });
    }
    cara.forEach(getcara);
  }
});
