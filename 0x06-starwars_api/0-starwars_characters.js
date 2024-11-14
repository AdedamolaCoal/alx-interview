#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
    if (error || response.statusCode !== 200) {
        console.error('Error fetching data:', error);
        return;
    }

    const data = JSON.parse(body);
    const characterUrls = data.characters;

    characterUrls.forEach(url => {
        request(url, (error, response, body) => {
            if (!error && response.statusCode === 200) {
                const characterData = JSON.parse(body);
                console.log(characterData.name);
            }
        });
    });
});
