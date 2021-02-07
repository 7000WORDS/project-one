print("this is a sign up program")
print("put a space after each segment")
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
gender = input("gender: ")
form = input("form class: ")


d = open("mystuff.txt", "a+")


d.write(first_name)

d.write(last_name) 

d.write(gender)

d.write(form)
