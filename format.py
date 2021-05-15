# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))
print("Hello {it}, I am {name}".format(it="world", name="Hung"))

print("Hello, my name is {:10}. Nice to meet you".format("Hung"))
print("Hello, my name is {:>10}. Nice to meet you".format("Hung"))
print("Hello, my name is {:<10}. Nice to meet you".format("Hung"))
print("Hello, my name is {:^10}. Nice to meet you".format("Hung"))

pi = 3.1443643

print("The number pi is {:.2f}".format(pi))
print("The number is {:,}".format(10000))
print("The number is {:b}".format(10000))
print("The number is {:o}".format(10000))
print("The number is {:X}".format(10000))
print("The number is {:E}".format(10000))