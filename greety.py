"""
greet(name) - context: human name works best, will take any type argument and return it embedded in a greeting.  
"""
def greet(name):
    print(f"Hello, {name}! Welcome to my greety script.")

"""
name_input - prompts the user to enter their name, returns it in variable name_inputted
"""
def name_input():
    name_inputted = input("Tell me your name: ")
    return name_inputted

name = name_input()
greet(name)



