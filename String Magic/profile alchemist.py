"""
Project: Student Information Profile Card
Author: Dahlia Mphalo
Description: This script .
"""

first_name = input("Enter your first name: " ).strip()
last_name = input("Enter your last name: " ).strip()
bio = input("Please Enter a short description about yourself" ).strip()

Username = first_name[0].lower() + last_name.lower()
Full_name = first_name.title() + " " + last_name.title()

bio = bio.replace("I am", "I'm")
bio_characters = len(bio)

print(f" hi, welcome your first name is {first_name} and your last name is {last_name}, ")
print( f" Meaning your username is {Username} and your full name is {Full_name}. ")
print(f"Your bio has {bio_characters} characters.")
