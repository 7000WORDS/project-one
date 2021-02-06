def func():
    for x in range(2):
        print("X ",end="")

    for x in range(2):
        print(func())


func()
