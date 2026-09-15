
# Now to make it more advanceed and give users options to round off to the nearest decimal place:

#Basic Calculator

# Input from user
a = input("Enter the first number: ")
b = input("Enter the second number: ")

# Processing the input and performing calculations
sum = float(a) + float(b)
sub = float(a) - float(b)
div = float(a) / float(b)
Mult = float(a) * float(b)


Print(f'Hi would you like to use {calculator_fx.lower()} or {basic_calculator.lower()}?')
input("Enter your choice: ")

if basic_calculator
    print("You have selected the Basic Calculator.")
    # Here you can add the code for the basic calculator functionality
    # Outputting the results
    print (f"The sum of {a} + {b} is: {sum}")
    print (f"The difference of {a} - {b} is: {sub}")
    print (f"The product of {a} * {b} is: {Mult}")
    print (f"The quotient of {a} / {b} is: {div}")

elif calculator_fx
    print("You have selected Calculator 2.0. the smart calculator that can round off to the nearest decimal place.")
    # Here you can add the code for the advanced calculator functionality
    # Outputting the results
    print (f"The sum of {a} + {b} is: {sum:.2f}")
    print (f"The difference of {a} - {b} is: {sub:.2f}")
    print (f"The product of {a} * {b} is: {Mult:.2f}")
    print (f"The quotient of {a} / {b} is: {div:.2f}")

 else print("Invalid choice. Please select either 'basic_calculator' or 'calculator_2.0'.")
