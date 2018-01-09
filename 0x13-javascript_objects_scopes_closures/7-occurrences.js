#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let count = list.reduce(function(list_num, value) {
    return list_num + (value === searchElement);
  }, 0);
  return count;
}
