from .message import Message

class Calculator:
    
    # BASIC OPERATIONS
    def add(n1: int|float, n2: int|float) -> int|float:
        return (n1 + n2)

    def subtract(n1: int|float, n2: int|float) -> int|float:
        return (n1 - n2)

    def multiply(n1: int|float, n2: int|float) -> int|float:
        return (n1 * n2)

    def divide(n1: int|float, n2: int|float) -> int|float:
        return (n1 / n2)


    # MULTIPLY ALL NUMBERS FROM A LIST
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


    # SUM ALL NUMBERS FROM A LIST
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


    # CALC AVERAGE OF A LIST OF NUMBERS
    def average(array: list[int|float]) -> int|float:
        try:   
            average = sum(array) / len(array)

            if '.0' in str(average):
                average = int( str(average).replace('.0', '') )

            return average

        except TypeError:
            print('\033[1;31m[WARNING]\033[0m \033[31mcalcAverage expect an list[int|float] in parameter\033[0m')


    # FACTORIAL
    def factorial(number: int) -> int:
        return Calculator.prod(range(1, number+1))
