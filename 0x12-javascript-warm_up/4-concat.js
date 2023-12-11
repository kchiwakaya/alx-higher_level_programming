#!/usr/bin/node
const process = require('process');

let value1;
let value2;
if (process.argv.length > 2) {
  if (process.argv.length > 3) {
    value2 = process.argv[3];
  }
  value1 = process.argv[2];
}
console.log(value1 + ' is ' + value2);

