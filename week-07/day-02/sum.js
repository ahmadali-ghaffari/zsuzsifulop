'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

var numbers = [1, 2, 3];
var sum_amount = 0;
function sum(numbers_to_sum) {
    var i = 0;
    for (i = 0; i < numbers_to_sum.length; i++){
        sum_amount += numbers_to_sum[i];
    }
    return sum_amount;
}
sum(numbers);

