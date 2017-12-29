'use strict';
// - Create a variable named `nimals`
//   with the following content: `["kuty", "macsk", "cic"]`
// - Add all elements an `"a"` at the end
// - try to use built in functions instead of loops

var nimals = ["kuty", "macsk", "cic"];

var plus_a = nimals.map(function (x) {
    return x + 'a';
});
console.log(plus_a);
