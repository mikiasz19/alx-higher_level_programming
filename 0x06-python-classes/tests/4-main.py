#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {0} for size: {1}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {0} for size: {1}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {0} for size: {1}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
