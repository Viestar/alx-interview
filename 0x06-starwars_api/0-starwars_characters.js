#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie
 */
const request = require('request');
const film_id = process.argv[2];
if (!film_id  || isNaN(film_id)) {
  process.exit(1);
}
const url = `https://swapi-api.hbtn.io/api/films/${film_id}`;

request(url, (error, res, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characterList = [];

  const starwars = JSON.parse(body);
  const characters = starwars.characters;

  characters.forEach((character) => {
    const url = character;
    const promise = new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        const starwars = JSON.parse(body);
        resolve(starwars.name);
      });
    });
    characterList.push(promise);
  });
  Promise.all(characterList).then((values) => {
    values.forEach((value) => {
      console.log(value);
    });
  }).catch((error) => {
    console.log(error);
  });
});
