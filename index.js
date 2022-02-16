import Fetch from '.node-fetch';

Fetch('http://127.0.0.1:5000/')
    .then(response => response.json())
    .then(json => console.log(json))