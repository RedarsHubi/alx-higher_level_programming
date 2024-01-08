#!/usr/bin/node
function lafac (a) {
  if ((Number.isNaN(a)) || (a === 1)) {
    return 1;
  }
  return lafac(a - 1) * a;
}

console.log(lafac(parseInt(process.argv[2])));
