# reduce()  =  apply a function to an iterable and reduce it to a single cumulative value
#       performs function on first two elements and repeats process util 1 value remains

# reduce(function, iterable)

import functools
letters = ["H", "E", "L", "L", "O"]
_fun = lambda x, y,: x + y
word = functools.reduce(_fun, letters)
print(word)