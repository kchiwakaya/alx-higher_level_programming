#!/usr/bin/node
const process = require('process');
let con = "Not  a number";
let num;

if (process.argv.length > 2) {
  num = parseInt(process.argv[2]);
  if (!isNaN(num)) {
    con = 'My number: ' + String(num);
  }
}
console.log(con);

