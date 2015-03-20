#!/usr/bin/python

name = raw_input("Enter your name: ")

print("How are you today, " + name + "?")
print("1. good")
print("2. OK")
print("3. terrible")

mood = int(raw_input(""))

if mood == 1:
  print("Excellent " + name + "! Continue having a great day!")
elif mood == 2:
  print("Go outside and get some sun " + name + "; that'll make you feel better!")
elif mood == 3:
  print("Cheer up " + name + ", things will get better!")
else:
  print("Invalid input!")
