'use strict';
// When saving this quote a disk error has occured. Please fix it.
// Add "always takes longer than" to between the words "It" and "you"

var quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law.";
var quote2 = quote.slice(0, 21) + "always takes longer than " + quote.slice(21); 
console.log(quote2);
