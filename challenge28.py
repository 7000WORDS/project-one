import random
name_one = input("enter 5 names: ")
name_two = input("two: ")
name_three = input("three: ")
name_four = input("four: ")
name_five = input("five: ")

array =(name_one,name_two,name_three,name_four,name_five)
x = random.choice(array)
print(x)