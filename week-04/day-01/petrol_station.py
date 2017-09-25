# Petrol Station

# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

class Station():
    gas_amount = 1000
    

class Car():
    capacity = 100 
    def refill(self):
        Station.gas_amount -= self.capacity

Audi = Car()
Audi.refill()

print(Station.gas_amount)
print(Car.capacity)