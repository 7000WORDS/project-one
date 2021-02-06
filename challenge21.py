name = input("enter your name: ")
print("Hello " + name.capitalize())
length = input("what are you converting from: ")
if length == "inches":
    def func():
        x = int(input("enter the number in inches: "))
        z = x * 2.54
        print(str(round(z)) + " centimetres (rounded)")
    func()

if length == "centimetres":
    def func():
        x = int(input("enter the number in centimetres: "))
        y = x * 0.393700787
        print(str(round(y)) + " inches(rounded)")
    func()