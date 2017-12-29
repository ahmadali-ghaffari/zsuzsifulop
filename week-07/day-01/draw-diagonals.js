var lineCount = 6;
var i;
var j;
var string = "";

for (i = 0; i < lineCount; i++) {
    for (j = 0; j < lineCount; j++) {
        if (i === 0 || j === 0 || j === lineCount - 1 || i === lineCount - 1 || i === j) {
            string += "%";
        } else {
            string += " ";
        }
    }
    console.log(string);
    string = "";
}
