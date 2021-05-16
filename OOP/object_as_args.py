class Car:

    color = None

class Motorcycle:
    color = None

def change_color(car, color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
motorcycle = Motorcycle()

change_color(car_1, 'red')
change_color(car_2, 'white')
change_color(car_3, 'blue')
change_color(motorcycle, 'yellow')

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(motorcycle.color)