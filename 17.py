class Calculator:
    def __init__(self):
        self.__result = 0  # Private attribute to store the result

    # Method to perform addition
    def add(self, value):
        self.__result += value
        return self.__result

    # Method to perform subtraction
    def subtract(self, value):
        self.__result -= value
        return self.__result

    # Method to get the current result
    def get_result(self):
        return self.__result

# Create an instance of the Calculator class
calc = Calculator()

# Perform addition and subtraction
print("After adding 10:", calc.add(10))        # Output: 10
print("After subtracting 3:", calc.subtract(3)) # Output: 7
print("Final result:", calc.get_result())       # Output: 7
