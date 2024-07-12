#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie. Status code:', response.statusCode);
    return;
  }

  const characters = body.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (error, response, body) => {
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error('Failed to fetch character. Status code:', response.statusCode);
        return;
      }

      console.log(body.name);
    });
  });
});
