#!/usr/bin/node

const moveId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + moveId;
let people = [];
const names = [];

const requestCharacters = async () => {
    await new Promise(request(filmEndPoint, (err, res, body) => {
        if (err || res.statusCode !== 200) {
            console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
            const jsonBody = JSON.parse(body);
            people = jsonBody.characters;
            resolve();
        }
    }));
};