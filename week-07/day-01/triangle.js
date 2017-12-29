'use strict';

var lineCount = 4;

// Write a program that draws a
// triangle like this:
//
// *
// **
// ***
// ****
//
// The triangle should have as many lines as lineCount is
var stars = "";
var i = 1;
for (i; i <= lineCount; i++) {
    stars += "*"
    console.log(stars);
}
