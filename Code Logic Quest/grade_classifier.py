"""
Project: Code Logic - Student Grade Classifier
Author: Dahlia Mphalo
Description: A Python program that collects a learner's name and marks for  three subjects, 
             calculates the average, assigns a letter grade(A/B/C/D/F) and a Pass/Fail status using conditionals, flags
             any subject mark below 40 as 'needs intervention', and displays
             a formatte
"""

Name = input("What's your name? ")



Subject1 = float(input("Enter your mark for Subject 1: "))
Subject1_total = float(input("Enter the total marks for Subject 1: "))

Subject2 = float(input("Enter your mark for Subject 2: "))
Subject2_total = float(input("Enter the total marks for Subject 2: "))

Subject3 = float(input("Enter your mark for Subject 3: "))
Subject3_total = float(input("Enter the total marks for Subject 3: "))


Average_mark = (Subject1 + Subject2 + Subject3) / 3

#Now how our code will reason
if Average_mark >= 50:
    print("STATUS: passed!")
elif:
    print("STATUS: failed!")

else Average_mark <= 40]:
    print("You need intervention!")


if Average_mark >= 80:
    print("GRADE A")
    print("You're cum Laude!")

elif Average_mark >= 70:
    print("GRADE B")
    print("You've achieved a distinction!")

elif Average_mark >= 60:
    print("GRADE C")
    print("You've passed with merit!")

elif Average_mark >= 50:
    print("GRADE D")
    print("You've barely passed!")

else:
    print("GRADE F")
    print("Come on now :(!")

print(f"Your average mark is: {Average_mark}%")
