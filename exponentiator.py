"""
Can we do comments at some point?  Raises num1 to power num2.
"""
def exponentiate(num1, num2):
    return num1 ** num2

"""
Accepts one input, number to raise to 4th power. Calls exponentiate with 4th power set.
"""
def raise_to_the_fourth(num1):
    return exponentiate(num1, 4)

"""

"""
square = lambda num1: exponentiate(num1, 2)
cube = lambda num2: exponentiate(num2, 3)

print(square(2))
print(cube(2))
print(raise_to_the_fourth(2))
