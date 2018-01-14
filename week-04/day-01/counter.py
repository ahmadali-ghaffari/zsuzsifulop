# Create Counter class
# which has an integer field value
# when creating it should have a default value 0 or we can specify it when creating  # nopep8
# we can add(number) to this counter another whole number
# or we can add() without parameters just increasing the counter's value by one
# and we can get() the current value
# also we can reset() the value to the initial value
# Check if everything is working fine with the proper test
# Download test_counter.py and place it next to your solution
# Run the test file as a usual python program


class Counter():
    def __init__(self, start=0):
        self.integer = start

    def add(self, number=None):
        if number is None:
            self.integer += 1
        else:
            self.integer += int(number)

    def get(self):
        print(self.integer)
        return self.integer

    def reset(self):
        self.__init__()

count = Counter()
count.add(3)
count.get()
count.reset()
count.get()