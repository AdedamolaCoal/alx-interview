#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as an argument.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error('Error fetching character data:', characterError);
        return;
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});