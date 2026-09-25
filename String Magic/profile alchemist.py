"""
Project: String Alchemy - A Text-Processing Engine
Author: Dahlia Mphalo
Description: This script is a backend simulation that transforms raw user input into sanitized profile data. 
             Demonstrates string manipulation, username generation, and dynamic f-string formatting.
"""

# 1. Collecting and "Stripping" raw input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
bio = input("Please enter a short bio: ").strip()

# 2. The Transformation Magic
# Creating a username (first initial + last name)
username = (first_name[0] + last_name).lower()
full_name = f"{first_name.title()} {last_name.title()}"

# Refining the bio
refined_bio = bio.replace("I am", "I'm")
bio_characters = len(refined_bio)

# 3. The Polished Output
print(f"\n--- User Profile Generated  ---")
print(f" hi, welcome your first name is {first_name} and your last name is {last_name}, ")
print(f" Meaning your username on the system {username} and your full name is {full_name}. ")
print(f" Refined Bio: \"{refined_bio}\"")
print(f" Your new bio has {bio_characters} characters.")
