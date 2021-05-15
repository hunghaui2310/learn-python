# math function
import math

pi = 3.14
x = 1
y = 2
z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 3))
# print(math.sqrt(420))
# print(max(x, y, z))
print(min(x, y, z))

# slice function
name = 'Hung NN'
first_name = name[:4]
last_name = name[5:]
reversed_name = name[::-1]
print("first name = ", first_name, ",last name = ", last_name, ",reversed name = ", reversed_name)

website1 = 'http://google.com'
website2 = 'http://facebook.com'

slice = slice(7, -4)
website1 = website1[slice]
website2 = website2[slice]
print(website1, website2)