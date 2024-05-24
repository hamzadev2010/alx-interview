#!/usr/bin/node
/* script that prints all characters of a Star Wars movie*/

const request = require('request');
const starwarsurl = 'https://swapi-api.alx-tools.com/api/films/${fId}';
const fId = process.argv[2].toString();

request(starwarsurl, async (error, rs, body) => {
  err && console.log(err);

  const charactersArray = (JSON.parse(res.body).characters);
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (error, rs, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
