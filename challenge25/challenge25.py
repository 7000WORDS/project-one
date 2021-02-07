print("this is a sign up program")
print("put a space after each segment")
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
gender = input("gender: ")
form = input("form class: ")


d = open("mystuff.txt", "w+")


d.write("first name = "+first_name + "\n")

d.write("last name = "+last_name + "\n")

d.write("gender = "+gender + "\n")

d.write("form = "+form + "\n")
