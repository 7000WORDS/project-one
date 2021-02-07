name = input("enter your name: ")
print("hello " + name)
print("this is a maths quiz")
question_1 = int(input("what is 5 + 9: "))
question_2 = int(input("what is 3 x 11: "))
question_3 = int(input("what is 6 divided by 3: "))

if question_1 == 14:
    print("you got it right")
else:
    print("you got it wrong")

if question_2 == 33:
    print("you got it right")
else:
    print("you got it wrong")

if question_3 == 2:
    print("you got it right")
else:
    print("you got it wrong")


def func():
    f = open("maths_quiz.txt", "x")
    f.writelines(name + "\n")
    f.writelines(str(question_1) + "\n")
    f.writelines(str(question_2) + "\n")
    f.writelines(str(question_3) + "\n")


func()
