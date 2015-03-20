#!/usr/bin/python

name = raw_input("Enter your name: ")

print("1. good")
print("2. OK")
print("3. terrible")

valid = 0

while not valid:
  try:
    mood = int(raw_input("How are you today, " + name + "? "))
  except:
    print("Invalid input!")
    exit()

  if mood == 1:
    print("Excellent " + name + "! Continue having a great day!")
    valid = 1
  elif mood == 2:
    print("Go outside and get some sun " + name + "; that'll make you feel better!")
    valid = 1
  elif mood == 3:
    print("Cheer up " + name + ", things will get better!")
    valid = 1
  else:
    print("Invalid input!")
