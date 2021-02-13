from io import open
from typing import ValuesView

name = ("name: ")
people = ("how many people are coming: ")
tasks = ("how many things are you buying: ")
clothes = ("how many clothes are you packing: ")
currency = ("buy foreign currency: ")
visa_up_date = ("Is your passport up to date: ")
ticket = ("have you bought your ticket: ")
f = open("holiday.txt","a+")
f . write(name + "\n")
f . write(people + "\n")
f . write(tasks + "\n")
f . write(clothes + "\n")
f . write(currency + "\n")
f . write(visa_up_date + "\n")
f . write(ticket + "\n")


