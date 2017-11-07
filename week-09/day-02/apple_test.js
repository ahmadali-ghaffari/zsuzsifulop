'use strict';

var test = require('tape');
var apple = require('./apple.js');

test('string test', function (t) {
  t.equal(typeof apple.getApple(), 'string');
  t.end();
});