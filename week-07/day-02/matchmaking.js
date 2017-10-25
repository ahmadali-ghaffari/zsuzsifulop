'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];
var order = [];
var i = 0;
var j = 0;

for (i = 0; i <boys.length; i++){
        order += girls[i] + " " + boys[i] +" "
    }


console.log(order);