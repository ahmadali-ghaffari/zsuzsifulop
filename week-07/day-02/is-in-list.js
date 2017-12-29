'use strict';
// Check if array contains all of the following elements: 4,8,12,16
// Create a 'numChecker' function that accepts 'listOfNumbers' as an input
// it should return "true" if it contains all, otherwise "false"

var arr1 = [2, 4, 6, 8, 10, 12, 14, 16];
var arr2 = [2, 8, 412, 16];
var i = 0;
var j = 0;
var bool = true;

for (i = 0; i < arr1.length; i++) {
    for (j = 0; j < arr2.length; j++) {
        if (arr1[i] !== arr2[j]) {
            bool = false;
        }
    }
}
if (bool) {
    console.log("true");
} else {
    console.log("false");
}
