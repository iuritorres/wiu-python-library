class Calculator:
    
    # basic operations
    def add      (num1: int|float, num2: int|float) -> int|float : return (num1 + num2)
    def subtract (num1: int|float, num2: int|float) -> int|float : return (num1 - num2)
    def multiply (num1: int|float, num2: int|float) -> int|float : return (num1 * num2)
    def divide   (num1: int|float, num2: int|float) -> int|float : return (num1 / num2)

    # product of a list of numbers
    def product(array: list) -> int|float:
        result = array[0]

        for index in range(len(array)):
            if (index + 1) == len(array):
                break

            else:
                result *= array[index + 1]

        return result



if __name__ == '__main__':
    prod = Calculator.product([3, 3, 3])
    print(prod)
