class Animal {
    
      constructor(hunger, thirst) {
        this.hunger = 5;
        this.thirsty = 5;
      }
      eat() {
          this.hunger -= 1;
      }

      drink() {
          this.thirst -= 1;
      }
      play(){
          this.thirst -=1;
          this.hunger -= 1;
      }
    };

    class Farm {

        constructor(slot){
            this.slot = slot;
            this.animal_list = [];
        }

        breed(){
            if (this.slot > 0){
                var animal = new Animal();
                this.animal_list.push(animal);
            } else {
                console.log("No place for anilmals!")
            }
        }
        slaghter (){
            this.animal_list.sort(function(a, b) {
                return b.hunger - a.hunger;
            });
            this.animal_list.splice(this.animal_list.length, 1);
        }
        current_state() {
            console.log("The farm has " + this.animal_list.length +" living animals, we are bankrupt.");
        }
        progress(){
            for (var i = 0; i < this.animal_list.length; i++){
                if (Math.random() > 0.5){
                    this.animal_list.splice(this.animal_list[i], 1);
                }
            }
            console.log("Number of sheeps: " + this.animal_list.length);
                if (this.animal_list.length < 1){
                    console.log("bankrupt");
                } else if (this.animal_list.length === this.slot) {
                    console.log("full")
                } else if (this.animal_list.length > 0 || this.animal_list.length < this.slot){
                    console.log("ok")
                }
        }
    }
    

    var farm = new Farm(2);
    farm.breed();
    farm.breed();
    
    farm.progress();
    