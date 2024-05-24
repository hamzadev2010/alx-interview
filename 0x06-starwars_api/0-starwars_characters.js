#!/usr/bin/node
/* script that prints all characters of a Star Wars movie*/

const request = require('request');
const starwarsurl = 'https://swapi-api.alx-tools.com/api/films/${fId}';
const fId = process.argv[2].toString();

request(starwarsurl, function (error, _, body) {
  if (error) {
    console.error(error);
    return;
  }

  const objects = JSON.parse(body);
  const characters = objects.characters;
  printCharacters(characters);
});


function printCharacters(characters, index = 0) {
  request(characters[index], function (error, _, body) {
    if (error) {
      console.error(error);
      return;
    }

    console.log(JSON.parse(body).name);
    if (++index < characters.length) {
      printCharacters(characters, index);
    }
  });
}
