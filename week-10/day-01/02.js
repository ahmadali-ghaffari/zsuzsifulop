'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

const Rectangle = function (a, b){
    this.a = a;
    this.b = b;
}

Rectangle.prototype.getArea = function(){
    return this.a * this.b
}

Rectangle.prototype.getCircumference = function(){
    return 2 * this.a + 2 * this.b 
}

let a = new Rectangle(3,4);
let b =  a.getArea()



