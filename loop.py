# while loop

name = ""

while not name:
    name = input("Enter your name: ")

print("Hello " + name)

# for loop

# for i in range(10):
#     print(i)

for i in range(50, 100, 2):
    print(i)

# nested loop

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("enter  a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# loop control statement

# break: used to terminate the loop entirely
# continue: skip to the next iteration the loop
# pass: does thing, acts as a placeholder

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)