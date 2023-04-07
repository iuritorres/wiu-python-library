# WIU Python Library

## Usage
- import

```
from wiu import Calculator as calc

mult = calc.multiply(2, 3)
print(mult)
```

returns:
> 6

## Features

- Basic operations
```
add = calc.add(2, 3)
sub = calc.subtract(2, 3)
mult = calc.multiply(2, 3)
div = calc.divide(2, 3)

print(add, sub, mult, div)
```
returns:
> 5 -1 6 0.6666666666666666

- Product of many numbers
```
my_numbers = [1, 3, 6, 4, 5, 9]

prod = calc.product(my_numbers)
print(prod)
```
returns:
> 3240

- Factorial
```
fact = calc.factorial(6)
print(fact)
```
returns:
> 720