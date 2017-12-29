
// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//

var style01 = "% % % %";
var style02 = " % % % %";

var i;

for (i = 1; i < 9; i++) {
    if (i % 2 === 0) {
        console.log(style01);
    } else {
        console.log(style02);
    }
}
