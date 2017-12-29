'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

var numbers = [1, 2, 3, 7];
var factorial_value = 1;
function factorial(numbers_to_multiply) {
    var i = 0;
    for (i = 0; i < numbers_to_multiply.length; i++) {
        factorial_value *= numbers_to_multiply[i];
    }
    console.log(factorial_value);
    return factorial_value;
}
factorial(numbers);
