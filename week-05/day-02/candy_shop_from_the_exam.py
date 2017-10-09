# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies, store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"
class Sweets:
    def __init__(self, sweet_type):
        if sweet_type == "lollipop":
            self.sugar = 5
            self.price = 10
            self.name = "lollipop"
        elif sweet_type == "candy":
            self.sugar = 10
            self.price = 20
            self.name = "candy"

class CandyShop:
    candy_list = []
    income = 0
    def __init__(self, amount_candy_sugar):
        self.amount_candy_sugar = amount_candy_sugar

    def create_sweets(self, sweet_type):
        self.candy_list.append(Sweets(sweet_type))
        self.amount_candy_sugar -= self.candy_list[-1].sugar

    def raise_prices(self, persentage):
        for sweet in self.candy_list:
            sweet.price += sweet.price * (persentage / 100)
    
    def sweet_number_calc(self, sweet_type):
        self.sweet_number = 0
        for sweet in self.candy_list:
            if sweet.name == sweet_type:
                self.sweet_number += 1
        return self.sweet_number
    
    def sell(self, sweet_type, amount):
        while amount > 0 and self.sweet_number_calc(sweet_type) != 0:
            for i in range(len(self.candy_list)):
                if self.candy_list[i].name == sweet_type:
                    self.income += self.candy_list[i].price
                    del self.candy_list[i]
                    amount -= 1
                    break
    
    def buy_sugar(self, amount):
        self.amount_candy_sugar += amount
        self.income -= amount / 10

    def __repr__(self):
        return "Inventory: {} candies, lollipops {}, Income {}, Sugar: {}gr ".format(self.sweet_number_calc("candy"), self.sweet_number_calc("lollipop"), self.income, self.amount_candy_sugar)

candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
#print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)

#print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"