"""
Project: Phone Directory Search
Author: Dahlia Mphalo
Description: A mini data directory program that stores 3 friends and their phone numbers in a dictionary. 
             It asks the user for a name, checks if the name exists as a key, and prints their number if found, 
             or a "not found" message if they aren't in the directory.
"""

# Adding a key Value dictionary 
contacts = { "Amanda": "0821112222" ,
             "Brian": "0832223333" ,
             "Catherine": "0843334444" }

# Giving user access/ flexibility to serach contact list insted of having to manually search
search_name = input("Enter the name of the friend you want to look up: ")

#Giving that "flexibility" a logic how to operate 
if search_name in contacts:
    print(f"Found! {search_name}'s number is {contacts[search_name]}.")
else:
    print("Contact not found.")
