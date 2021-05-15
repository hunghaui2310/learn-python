# function: a block of code which is executed only when it is called

def hello(name):
    print("Hello World!")
    print("Hello " + name)

# hello()
hello("Hung")

def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 2))

# keyword argument: argument preceded by an identifier when we pass them to function
#     The order of the arguments doesn't matter, unlike positional arguments
#       Python knows the name of the arguments that our function receives

def helloArgument(first, middle, last):
    print("Hello "+ first + " " + middle + " " + last)

helloArgument(last="Hung", first="Nguyen", middle="Ngoc")

# *args: parameter that will pack all arguments into a tuple
#        useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,4,56))

# **kwargs: parameter that will pack all arguments into a dictionary
#       useful so that a function can accept a varying amount of keyword arguments

def helloKwArgs(**kwargs):
    #   print("Hello" + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, val in kwargs.items():
        print(val, end=" ")

helloKwArgs(title="Mr.", last="Hung", first="Nguyen", middle="Ngoc")
