'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

var parameters_to_write_out = ["Zsuzsi", "Fülöp"];

function printer(parameter) {
    var i = 0;
    for (i = 0; i < parameter.length; i++) {
        console.log(parameter[i]);
    }
}

printer(parameters_to_write_out);
