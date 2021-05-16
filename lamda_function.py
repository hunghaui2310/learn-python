# lambda function = function written in 1 line using lambda keyword
#           accepts any number of arguments, but only has one expression
#           (think of it as a shortcut)
#           (useful if needed for a short period of time, throw-away)

# def double(x):
#     return x * 2
#
# print(double(5))

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
age_check = lambda age: True if age >= 18 else False
full_name = lambda first_name, last_name: first_name + " " + last_name

print(double(5))
print(multiply(5, 6))
print(add(2, 3, 4))
print(age_check(15))
print(full_name("Hung", "NN"))