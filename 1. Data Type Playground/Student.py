"""
Project: Student Information Profile Card
Author: Dahlia Mphalo
Description: This script collects and processes user data, demonstrating 
mastery of string manipulation, float rounding, and data type casting.
"""

First_name = input("What's your First name?")
Surname = input("What's your Surname?")
age = int(input("How old are you?")) # Cast to integer immediately
Favourite_Number = float(input("What's your favourite number?"))
months = age * 12

print( f"Welcome, {First_name.upper()} {Surname.title()}, you have lived for {months} months thus far. Could your favourite number be {Favourite_Number:.2f}? when rounded to two decimal places.   "  )

#Showing off data type knowledge
print(f"\nSystem Logs: Data Types")
print(f" Name: {type(First_name)}")
print(f" Age: {type(age)}")
print(f" Fav_Num: {type(Favourite_Number)}")
print(f" Months Lived: {type(months)}")
