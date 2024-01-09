#!/usr/bin/node
exports.esrever = function (list) {
  const rlist = [];
  let i = list.length - 1;

  for (i; i >= 0; i--) {
    rlist.push(list[i]);
  }
  return rlist;
};
