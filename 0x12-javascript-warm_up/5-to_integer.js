#!/usr/bin/node
const gharam = parseInt(process.argv[2]);

if (!isNaN(gharam)) {
  console.log('My number: ' + gharam);
} else {
  console.log('Not a number');
}
