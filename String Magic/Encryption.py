"""
Project:Secure Password Hint Tool
Author: Dahlia Mphalo
Description: Asks the user for a password, strips extra spaces, and prints a hint showing the first and last letters
             in uppercase
"""

Password = input("Please Enter your password ").strip()

hint =  f"your passwrord starts with {Password[0].upper()} and ends with {Password[-1].upper() }"
print( hint)



