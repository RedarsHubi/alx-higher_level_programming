#!/usr/bin/node
let i = 0;
let j = 0;
const rip = parseInt(process.argv[2]);
if (Number.isNaN(rip)) {
  console.log('Missing size');
} else {
  for (i = 0; i < rip; i++) {
    let store = '';
    for (j = 0; j < rip; j++) {
      store += 'X';
    }
    console.log(store);
  }
}
