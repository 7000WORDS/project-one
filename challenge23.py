import math
name = input("enter your name: ")
print("hello " + name.capitalize())


def func():
    length = int(input("enter the length of the garden: "))
    width = int(input("enter the width of the garden: "))
    area = length * width
    print(area)

    radius = int(input("enter the radius of the circular flower bed: "))
    area_of_Circle = math.pi * math.pow(radius, 2)
    print(area_of_Circle)
    dif_area = str(round(area - area_of_Circle,2))
    print("you will need "+str(dif_area)+" metres squared of turf.")


func()
