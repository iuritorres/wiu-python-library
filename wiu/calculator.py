from .message import Message

class Calculator:
    
    # basic operations
    def add(n1: int|float, n2: int|float) -> int|float:
        return (n1 + n2)

    def subtract(n1: int|float, n2: int|float) -> int|float:
        return (n1 - n2)

    def multiply(n1: int|float, n2: int|float) -> int|float:
        return (n1 * n2)

    def divide(n1: int|float, n2: int|float) -> int|float:
        return (n1 / n2)

    # multiply all numbers from a list
    def prod(array: list[int|float]) -> int|float:
        try:
            accumulated = array[0]

            for index in range(len(array)):
                if (index + 1) == len(array):
                    break

                else:
                    accumulated *= array[index + 1]

            return accumulated

        except IndexError:
            Message.send_error("You can't pass an empty list")
    
    # sum all numbers from a list
    def sum(array: list[int|float]) -> int|float:
        try:
            accumulated = array[0]

            for index in range(len(array)):
                if (index + 1) == len(array):
                    break

                else:
                    accumulated += array[index + 1]

            return accumulated

        except IndexError:
            Message.send_error("You can't pass an empty list")


    # factorial
    def factorial(number: int) -> int:
        return Calculator.prod(range(1, number+1))
