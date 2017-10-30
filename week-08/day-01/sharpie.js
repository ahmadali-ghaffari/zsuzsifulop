class Sharpie {
    
      constructor(color, width) {
        this.color = color;
        this.width = width;
        this.inkAmount = 100;
      }
      use () {
          while (this.inkAmount >= this.width){
            this.inkAmount -= this.width;
            console.log(this.inkAmount);
          }
      }
    }
var sharpieone = new Sharpie("red", 27);
sharpieone.use();