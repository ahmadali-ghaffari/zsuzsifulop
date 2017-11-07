'use strict';

var test = require('tape');
var sum = require('./sum.js');

test('string test', function (t) {
    var actual = sum.sumElements([3]);
    var expected = 3;
    t.equal(actual, expected);
    t.end();
});