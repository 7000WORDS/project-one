name = input("enter your name: ")
print("hello "+ name.capitalize())
def func():
    dis = int(input("enter the distance in metres: "))
    time = int(input("enter the time in seconds: "))
    speed = dis/time
    print(str(round(speed)) + " m/s")
func()