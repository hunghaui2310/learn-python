# scope: The region that a variable is recognized
#   A variable is only available from inside the region it is created
#   A global and locally scoped versions of a variable can be created

name = "Hung"

def display_name():
    name = "code"
    print(name)

display_name()