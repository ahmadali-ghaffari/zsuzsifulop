class Fibonacci:

    def fibonacci(self, number):
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            return (self.fibonacci(number - 1) + self.fibonacci(number - 2))
