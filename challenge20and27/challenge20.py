name = input("enter your name: ")
print("hello "+name)
count = 0
count = 1

x = int(input("guess a number: "))
while x != 7:
    x = int(input("guess again: "))
    count = count + 1
    

    if x == 7:
        print("well done")


def func():
    f = open("C:\Programs\sch\challenge20and27\scores.txt", "a")
    f.write("name: " + name + "\n")
    f.write("tries: " + str(count)+ "\n")
func()