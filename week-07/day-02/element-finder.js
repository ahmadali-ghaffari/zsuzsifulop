'use strict';

// Check if the array contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

var numbers = [1, 2, 3, 4, 5, 7, 8];
var i = 0;
var x = false;

for (i = 0; i < numbers.length; i++) {
    if (numbers[i] === 7) {
        x = true;
    }
}
if (x) {
    console.log("Huray");
} else {
    console.log("Nooo");
}
