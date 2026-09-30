"""
Project: Basic smart Calculator 2.0 
Author: Dahlia Mphalo 
Description: A Python-based calculator that performs basic arithmetic with a user-controlled rounding feature. 
Demonstrates mastery of conditional logic (if/elif/else) and string sanitization (.strip(), .lower())
"""


# Define calculator options
basic_calculator ="Basic Calculator"
calculator_fx = "Calculator 2.0"

#Asking the user to choose between the two calculator options
print(f'Hi would you like to use {calculator_fx.lower()} or {basic_calculator.lower()}?')
choice = input("Enter your choice (basic / fx): ").lower().strip()

# Input from user
a = input("Enter the first number: ")
b = input("Enter the second number: ")

# Processing the input and performing calculations
sum_result = float(a) + float(b)
sub_result = float(a) - float(b)
div_result = float(a) / float(b)
Mult_result = float(a) * float(b)


if choice == "basic":
    print("You have selected the Basic Calculator.")
    # Here you can add the code for the basic calculator functionality
    # Outputting the results
    print (f"The sum of {a} + {b} is: {sum_result}")
    print (f"The difference of {a} - {b} is: {sub_result}")
    print (f"The product of {a} * {b} is: {Mult_result}")
    print (f"The quotient of {a} / {b} is: {div_result}")

elif choice == "fx":
    print("You have selected Calculator 2.0. the smart calculator that can round off to the nearest decimal place.")
    # Here you can add the code for the advanced calculator functionality
    # Outputting the results
    print (f"The sum of {a} + {b} is: {sum_result:.2f}")
    print (f"The difference of {a} - {b} is: {sub_result:.2f}")
    print (f"The product of {a} * {b} is: {Mult_result:.2f}")
    print (f"The quotient of {a} / {b} is: {div_result:.2f}")

else:
    print("Invalid choice. TRY AGAIN Please select either basic_calculator or calculator_2.0.")
